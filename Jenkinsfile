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
                credentialsId: 'dockerhub-credentials-test',
                usernameVariable: 'DOCKER_USER',
                passwordVariable: 'DOCKER_TOKEN'
            )
        ]) {
            powershell '''
                $user = $env:DOCKER_USER
                $token = $env:DOCKER_TOKEN

                Write-Host "Username matches expected value: $($user -ceq 'avi1707')"
                Write-Host "Token is present: $(-not [string]::IsNullOrEmpty($token))"
                Write-Host "Token length: $($token.Length)"
                Write-Host "Token has surrounding whitespace: $($token -ne $token.Trim())"

                $hash = [System.Security.Cryptography.SHA256]::Create()
                try {
                    $bytes = [System.Text.Encoding]::UTF8.GetBytes($token)
                    $digest = [Convert]::ToHexString($hash.ComputeHash($bytes))
                    Write-Host "Token fingerprint: $digest"
                } finally {
                    $hash.Dispose()
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
