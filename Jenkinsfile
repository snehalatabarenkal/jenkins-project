pipeline {
    agent any

    environment {
        SCANNER_HOME = tool 'sonar'
        DOCKER_IMAGE = 'devops830/python-app:latest'
    }

    stages {
        stage('Git Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/anjalikota10/jenkins-project.git'
            }
        }

        stage('Trivy FS Scan') {
            steps {
                sh 'trivy fs --format table -o fs-report.html .'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('sonar') {  
                    sh ''' $SCANNER_HOME/bin/sonar-scanner -Dsonar.projectKey=flaskdemo \
                    -Dsonar.projectName=flaskdemo -Dsonar.java.binaries=target '''
                }    
            }
        }

        stage('Build & Tag Docker Image') {
            steps {
                script {
                    withDockerRegistry(credentialsId: 'dockerhub', toolName: 'docker') {
                        sh "docker build -t ${DOCKER_IMAGE} ."
                    }
                }
            }
        }

        stage('Scan Docker Image by Trivy') {
            steps {
                sh "trivy image --format table -o image-report.html ${DOCKER_IMAGE}"
            }
        }

        stage('Push Docker Image to Private Repo') {
            steps {
                script {
                    withDockerRegistry(credentialsId: 'dockerhub', toolName: 'docker') {
                        sh "docker push ${DOCKER_IMAGE}"
                    }
                }
            }
        }
    }
}
