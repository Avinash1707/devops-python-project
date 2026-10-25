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

       ```groovy
stage('Login to Docker Hub') {
    steps {
        withCredentials([
            usernamePassword(
                credentialsId: 'dockerhub-credentials-test',
                usernameVariable: 'DOCKER_USER',
                passwordVariable: 'DOCKER_TOKEN'
            )
        ]) {
            powershell '''
                $ErrorActionPreference = "Stop"

                $user = $env:DOCKER_USER.Trim()
                $token = $env:DOCKER_TOKEN.Trim()

                if ($user -ne "avi1707") {
                    throw "Unexpected Docker Hub username"
                }

                if ([string]::IsNullOrWhiteSpace($token)) {
                    throw "Docker Hub token is empty"
                }

                $token | docker login --username $user --password-stdin

                if ($LASTEXITCODE -ne 0) {
                    throw "Docker Hub login failed"
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
