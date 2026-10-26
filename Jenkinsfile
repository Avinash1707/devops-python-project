
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
        stage('Test Docker Hub Authentication') {
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
                        echo DOCKER_HUB_AUTHENTICATION_SUCCEEDED
                    '''
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
