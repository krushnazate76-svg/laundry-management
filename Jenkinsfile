pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                echo 'Cloning Laundry Management System...'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Basic Test') {
            steps {
                bat 'python -m py_compile app.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t laundry-app .'
            }
        }

        stage('Deploy Container') {
            steps {
                bat 'docker stop laundry-container || exit /b 0'
                bat 'docker rm laundry-container || exit /b 0'
                bat 'docker run -d -p 5000:5000 --name laundry-container laundry-app'
            }
        }

        stage('Verify Deployment') {
            steps {
                bat 'docker ps'
            }
        }
    }

    post {
        success {
            echo 'Laundry Management System deployed successfully!'
        }

        failure {
            echo 'Pipeline failed. Check the Jenkins console output.'
        }
    }
}