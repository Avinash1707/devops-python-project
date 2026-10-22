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
        bat 'timeout /t 5 /nobreak'
        bat 'docker ps -a --filter name=jenkins-test-app'
        bat 'docker logs jenkins-test-app'
        bat 'curl.exe --fail http://127.0.0.1:8002/'
    }
}
}