pipeline {
    agent any

    environment {
        IMAGE_NAME = "port-scanner"
        CONTAINER_NAME = "port-scanner-container"
    }

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/SAGAR97619/port-scanner.git'
            }
        }

        stage('Build Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh '''
                docker stop $CONTAINER_NAME || true
                docker rm $CONTAINER_NAME || true
                '''
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                docker run -d -p 5000:5000 \
                --name $CONTAINER_NAME \
                $IMAGE_NAME
                '''
            }
        }
    }
}
