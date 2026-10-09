pipeline {
agent any


stages {
    stage('Clone Repository') {
        steps {
            checkout scm
            echo 'Repository cloned successfully'
        }
    }

    stage('Install Dependencies') {
        steps {
            bat '"C:\\Users\\Krushna\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m pip install -r requirements.txt'
        }
    }

    stage('Basic Test') {
        steps {
            bat '"C:\\Users\\Krushna\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m py_compile app.py'
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
        echo 'Pipeline failed. Check Console Output.'
    }
}


}
