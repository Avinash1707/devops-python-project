
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

        stage('Test Docker Hub Authentication') {
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
                        $docker = "C:\\Program Files\\Docker\\Docker\\resources\\bin\\docker.exe"
                        $config = Join-Path $env:WORKSPACE ".docker-auth-test"

                        New-Item -ItemType Directory -Path $config -Force | Out-Null

                        try {
                            $env:DOCKER_CONFIG = $config

                            $token | & $docker login --username $user --password-stdin

                            if ($LASTEXITCODE -ne 0) {
                                throw "Docker Hub authentication test failed"
                            }

                            Write-Output "PIPELINE AUTHENTICATION TEST SUCCEEDED"
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
            echo 'Docker Hub authentication test passed.'
        }

        failure {
            echo 'Authentication test failed. Check Console Output.'
        }
    }
}
