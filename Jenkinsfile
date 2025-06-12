pipeline {
    agent any

    environment {
        SCANNER_HOME = tool 'sonar-scanner'
    }

    stages {
        stage('Git Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/snehalatabarenkal/jenkins-project.git'
            }
        }

        stage('Trivy FS Scan') {
            steps {
                sh 'trivy fs --format table -o fs-report.html .'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    sh '''${SCANNER_HOME}/bin/sonar-scanner \
                    -Dsonar.projectKey=flaskdemo \
                    -Dsonar.projectName=flaskdemo \
                    -Dsonar.sources=.'''
                }
            }
        }

        stage('Build & Tag Docker Image') {
            steps {
                script {
                    withDockerRegistry(credentialsId: 'dockerhub', toolName: 'docker') {
                        sh 'docker build -t snehalatabarenkal/python-app:latest .'
                    }
                }
            }
        }

        stage('Scan Docker Image by Trivy') {
            steps {
                sh 'trivy image --format table -o image-report.html snehalatabarenkal/python-app:latest'
            }
                        
        }

        stage('Push Docker Image') {
            steps {
                script {
                    withDockerRegistry(credentialsId: 'dockerhub', toolName: 'docker') {
                        sh 'docker push snehalatabarenkal/python-app:latest'
                    }
                }
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '*.html', allowEmptyArchive: true
        }
    }
}
