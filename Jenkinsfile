pipeline {
    agent any

    environment {
        IMAGE = "port-scanner"
        CONTAINER = "port-scanner"
    }

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh 'docker rm -f $CONTAINER || true'
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                docker run -d -p 5000:5000 \
                --name $CONTAINER \
                $IMAGE
                '''
            }
        }
    }
}
