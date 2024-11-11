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


        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('sonar') {  
                    sh ''' $SCANNER_HOME/bin/sonar-scanner -Dsonar.projectKey=flaskdemo \
                    -Dsonar.projectName=flaskdemo -Dsonar.java.binaries=target '''
                }    
            }
        }

        stage('SonarQube Quality Gate') {
            steps {
                script {
                    def qualityGate = waitForQualityGate()
                    if (qualityGate.status != 'OK') {
                        error "Pipeline aborted due to SonarQube quality gate failure: ${qualityGate.status}"
                    }
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'npm install'
            }
        }

        stage('Trivy Filesystem Scan') {
            steps {
                // Runs a Trivy FS scan on the local filesystem to detect any vulnerabilities
                sh 'trivy fs . --exit-code 1 --severity HIGH,CRITICAL --output trivy-fs-report.txt'
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

        stage('Trivy Image Scan') {
            steps {
                // Runs a Trivy scan on the Docker image to check for vulnerabilities in the image layers
                sh 'trivy image ${DOCKER_IMAGE} --exit-code 1 --severity HIGH,CRITICAL --output trivy-image-report.txt'
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
