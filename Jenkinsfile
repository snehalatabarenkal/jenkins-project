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
                    withKubeConfig(caCertificate: '', clusterName: 'eks-cluster', contextName: '', credentialsId: 'k8-token', namespace: 'webapps', restrictKubeConfigAccess: false, serverUrl: 'https://04B476509F5549E80CF3A83B02F281E1.gr7.us-west-2.eks.amazonaws.com') {
                    sh 'kubectl apply -f deployment.yml -n webapps'
                    sleep 30
                        
                    }
                }
            }
        }
        
    }
}

