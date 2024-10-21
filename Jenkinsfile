pipeline {
    agent any

    environment {
        SCANNER_HOME= tool 'sonar'
    }

    stages {
        stage('git checkout') {
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

        stage('Build & Tag docker image') {
            steps {
                script{
                    withDockerRegistry(credentialsId: 'dockerhub', toolName: 'docker') {
                      sh 'docker build -t devops830/python-app:latest .'
                    } 
                }
            }
        }

        stage('Scan Docker image by Trivy') {
            steps {
                sh 'trivy image --format table -o image-report.html devops830/python-app:latest'
            }
        }

        stage('Push docker image') {
            steps {
                script{
                    withDockerRegistry(credentialsId: 'dockerhub', toolName: 'docker') {
                        sh 'docker push devops830/python-app:latest'
                    }
                }
            }
        }
        
    }
}

