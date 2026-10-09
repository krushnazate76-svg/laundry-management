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

  groovy
        stage('Build Docker Image') {
            steps {
                bat '"C:\\Users\\Krushna\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" build -t laundry-app .'
            }
        }

        stage('Deploy Container') {
            steps {
                bat '"C:\\Users\\Krushna\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" stop laundry-container || exit /b 0'
                bat '"C:\\Users\\Krushna\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" rm laundry-container || exit /b 0'
                bat '"C:\\Users\\Krushna\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" run -d -p 5000:5000 --name laundry-container laundry-app'
            }
        }

        stage('Verify Deployment') {
            steps {
                bat '"C:\\Users\\Krushna\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" ps'
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
