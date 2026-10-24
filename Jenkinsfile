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

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t %DOCKER_IMAGE%:latest .'
            }
        }

        stage('Login to Docker Hub') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-credentials',
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_TOKEN'
                    )
                ]) {
                    powershell '''
                        $ErrorActionPreference = "Stop"

                        $user = $env:DOCKER_USER.Trim()
                        $token = $env:DOCKER_TOKEN.Trim()

                        Write-Host "Docker username: $user"
                        Write-Host "Token present: $(-not [string]::IsNullOrWhiteSpace($token))"
                        Write-Host "Token length: $($token.Length)"

                        if ($user -ne "avi1707") {
                            throw "Unexpected Docker Hub username"
                        }

                        if ([string]::IsNullOrWhiteSpace($token)) {
                            throw "Docker Hub token is empty"
                        }

                        $token | docker login -u $user --password-stdin

                        if ($LASTEXITCODE -ne 0) {
                            exit $LASTEXITCODE
                        }
                    '''
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                bat 'docker push %DOCKER_IMAGE%:latest'
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution completed.'
        }

        success {
            echo 'Docker image published successfully!'
        }

        failure {
            echo 'Pipeline failed. Check Console Output for details.'
        }
    }
}
