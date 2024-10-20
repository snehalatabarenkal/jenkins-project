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
                    sh 'kubectl apply -f deployment.yaml -n webapps'
                    sleep 30
                        
                    }
                }
            }
        }
        
    }
}

