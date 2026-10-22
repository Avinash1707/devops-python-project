pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Source code is managed in GitHub.'
            }
        }

        stage('Python Test') {
            steps {
                bat 'python -m unittest test_app.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t devops-python-app .'
            }
        }

        stage('Test Application') {
            steps {
                bat 'docker rm -f jenkins-test-app 2>NUL || exit /b 0'
                bat 'docker run -d --name jenkins-test-app -p 8002:8000 devops-python-app'
                bat 'curl.exe --retry 10 --retry-connrefused --retry-delay 2 --fail http://127.0.0.1:8002/'
            }
        }
    }

    post {
        always {
            bat 'docker rm -f jenkins-test-app 2>NUL || exit /b 0'
            echo 'Pipeline execution completed.'
        }
    }
}