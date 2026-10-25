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

        stage('Login and Push to Docker Hub') {
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
                        $config = Join-Path $env:WORKSPACE ".docker-config"

                        New-Item -ItemType Directory -Path $config -Force | Out-Null

                        try {
                            $env:DOCKER_CONFIG = $config

                            $token | & "C:\\Program Files\\Docker\\Docker\\resources\\bin\\docker.exe" login --username $user --password-stdin

                            if ($LASTEXITCODE -ne 0) {
                                throw "Docker Hub login failed"
                            }

                            & "C:\\Program Files\\Docker\\Docker\\resources\\bin\\docker.exe" push "$($env:DOCKER_IMAGE):latest"

                            if ($LASTEXITCODE -ne 0) {
                                throw "Docker image push failed"
                            }
                        }
                        finally {
                            Remove-Item Env:DOCKER_CONFIG -ErrorAction SilentlyContinue
                            Remove-Item $config -Recurse -Force -ErrorAction SilentlyContinue
                        }
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
            echo 'Docker image published successfully!'
        }

        failure {
            echo 'Pipeline failed. Check Console Output for details.'
        }
    }
}
```
