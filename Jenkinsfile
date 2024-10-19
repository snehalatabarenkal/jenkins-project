pipeline {
    agent any
    stages {
        stage('git checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/anjalikota10/jenkins-project.git'
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

        stage('Push docker image') {
            steps {
                script{
                    withDockerRegistry(credentialsId: 'dockerhub', toolName: 'docker') {
                        sh 'docker push devops830/python-app:latest'
                    }
                }
            }
        }

        stage('Deploy to k8s') {
            steps {
                script{
                    sh 'kubectl apply -f deployment.yaml'
                }
            }
        }
        






    }
}

