pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'avi1707/devops-python-app'
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
stage('Verify Non-Root User') {
    steps {
        bat '''
            docker image inspect "%DOCKER_IMAGE%:latest" --format "{{.Config.User}}" > docker-user.txt
            set /p IMAGE_USER=<docker-user.txt
            if /I not "%IMAGE_USER%"=="appuser" (
                echo ERROR: Docker image is not configured to run as appuser
                exit /b 1
            )
            echo SUCCESS: Docker image runs as appuser
        '''
    }
}
    steps {
        bat '''
            "C:\\Users\\Avinash\\AppData\\Local\\Microsoft\\WinGet\\Links\\trivy.exe" image --scanners vuln --severity HIGH,CRITICAL --format table "%DOCKER_IMAGE%:latest"
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
    }

    post {
        always {
            echo 'Pipeline execution completed.'
        }

        success {
            echo 'Tests passed, security scan completed, and Docker image published successfully!'
        }

        failure {
            echo 'Pipeline failed. Check Console Output for details.'
        }
    }
}
