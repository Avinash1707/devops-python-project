pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'avi1707/devops-python-app'
        CONTAINER_NAME = 'python-app-deployment'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Avinash1707/devops-python-project.git'
            }
        }

        stage('Run Automated Tests') {
            steps {
                bat 'python -m unittest -v test_app.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t %DOCKER_IMAGE%:latest .'
            }
        }

        stage('Trivy Security Scan') {
            steps {
                bat '''
                    "C:\\Users\\Avinash\\AppData\\Local\\Microsoft\\WinGet\\Links\\trivy.exe" image --scanners vuln --severity HIGH,CRITICAL --format table "%DOCKER_IMAGE%:latest"
                '''
            }
        }

        stage('Verify Non-Root User') {
            steps {
                bat '''
                    @echo off
                    docker image inspect "%DOCKER_IMAGE%:latest" --format "{{.Config.User}}" > docker-user.txt
                    if errorlevel 1 exit /b 1

                    set /p IMAGE_USER=<docker-user.txt
                    if /I not "%IMAGE_USER%"=="appuser" (
                        echo ERROR: Docker image is not configured to run as appuser
                        exit /b 1
                    )

                    echo SUCCESS: Docker image runs as appuser
                '''
            }
        }

        stage('Login and Push to Docker Hub') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-credentials-test',
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_TOKEN'
                    )
                ]) {
                    bat '''
                        @echo off
                        echo %DOCKER_TOKEN% | docker login --username "%DOCKER_USER%" --password-stdin
                        if errorlevel 1 exit /b 1

                        docker push "%DOCKER_IMAGE%:latest"
                        if errorlevel 1 exit /b 1
                    '''
                }
            }
        }

        stage('Deploy Application') {
            steps {
                bat '''
                    @echo off

                    docker rm -f "%CONTAINER_NAME%" 2>nul

                    docker run -d --name "%CONTAINER_NAME%" --restart unless-stopped -p 8000:8000 "%DOCKER_IMAGE%:latest"
                    if errorlevel 1 exit /b 1

                    echo Application container started.
                '''
            }
        }

       
        stage('Health Check') {
            steps {
                powershell '''
                    $healthy = $false

                    for ($i = 1; $i -le 10; $i++) {
                        try {
                            $response = Invoke-WebRequest `
                                -UseBasicParsing `
                                -Uri "http://localhost:8000" `
                                -TimeoutSec 3

                            if ($response.StatusCode -eq 200) {
                                $healthy = $true
                                Write-Output "Application response: $($response.Content)"
                                break
                            }
                        }
                        catch {
                            Write-Output "Health check attempt $i failed. Retrying..."
                        }

                        Start-Sleep -Seconds 3
                    }

                    if (-not $healthy) {
                        Write-Error "Application health check failed."
                        docker logs $env:CONTAINER_NAME
                        exit 1
                    }

                    Write-Output "SUCCESS: Application health check passed."
                '''
            }
        }

    post {
        always {
            echo 'Pipeline execution completed.'
        }

        success {
            echo 'Tests passed, image scanned and published, deployment completed, and health check passed.'
        }

        failure {
            echo 'Pipeline failed. Check Console Output for details.'
        }
    }
}