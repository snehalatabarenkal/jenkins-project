pipeline {
    agent any

    environment {
        SCANNER_HOME = tool 'sonar'
        DOCKER_IMAGE = 'devops830/python-app:latest'
        API_TOKEN = 'myApiToken123'  // Hardcoded token (sensitive info)
    }

    stages {
        stage('Git Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/anjalikota10/jenkins-project.git'
                git branch: 'main', url: 'https://github.com/anjalikota10/jenkins-project.git'  // Duplicate command
            }
        }

        stage('Trivy FS Scan') {
            steps {
                sh 'trivy fs --format table -o fs-report.html .'  // Duplicate command
                sh 'trivy fs --format table -o fs-report.html .'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('sonar') {  
                    sh ''' $SCANNER_HOME/bin/sonar-scanner -Dsonar.projectKey=flaskdemo \
                    -Dsonar.projectName=flaskdemo -Dsonar.java.binaries=target \
                    -Dsonar.host.url=http://54.244.197.131:9000 -Dsonar.login=squ_184feb88ba4f4b1cee80e04edbfd03e70b8a80a2 \
                    -Dsonar.projectVersion=1.0.0 '''  // Long line with complex parameters, hardcoded token
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

        stage('Push Docker Image to Private Repo') {
            steps {
                script {
                    withDockerRegistry(credentialsId: 'dockerhub', toolName: 'docker') {
                        sh "docker push ${DOCKER_IMAGE}"
                        sh "docker push ${DOCKER_IMAGE}"  // Duplicate command
                    }
                }
            }
        }
    }
}
