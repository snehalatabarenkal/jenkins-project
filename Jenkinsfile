@Library('shared') _
pipeline {
    agent any

    environment {
        SCANNER_HOME = tool 'sonar-scanner'
        OWASP_DC_NVD_API_KEY = credentials('owasp-api-key')
    }

    stages {

        stage("Workspace cleanup") {
            steps {
                cleanWs()
            }
        }

        stage('Git: Code Checkout') {
            steps {
                script {
                    code_checkout("https://github.com/anjalikota10/jenkins-project.git", "main")
                }
            }
        }

        stage("Trivy: Filesystem scan") {
            steps {
                script {
                    trivy_scan()
                }
            }
        }

        stage("OWASP: Dependency Check") {
            steps {
                script {
                    try {
                        owasp_dependency("${OWASP_DC_NVD_API_KEY}")
                    } catch (Exception e) {
                        echo "OWASP Dependency Check failed: ${e.message}"
                    }
                }
            }
        }

        stage("SonarQube: Code Analysis") {
            steps {
                withSonarQubeEnv('sonar') {
                    script {
                        sonarqube_analysis("${SCANNER_HOME}", "flaskdemo", "flaskdemo")
                    }
                }
            }
        }

        stage("SonarQube: Code Quality Gates") {
            steps {
                script {
                    try {
                        timeout(time: 5, unit: 'MINUTES') {
                            waitForQualityGate abortPipeline: true
                        }
                    } catch (Exception e) {
                        echo "SonarQube Quality Gate failed: ${e.message}"
                        currentBuild.result = 'FAILURE'
                    }
                }
            }
        }

        stage('Build & Tag Docker Image') {
            steps {
                script {
                    withDockerRegistry(credentialsId: 'dockerhub', toolName: 'docker') {
                        sh "docker build -t devops830/python-app:latest ."
                    }
                }
            }
        }

        stage('Scan Docker Image by Trivy') {
            steps {
                sh "trivy image --format table -o image-report.html devops830/python-app:latest"
            }
        }

        stage('Push Docker Image to Private Repo') {
            steps {
                script {
                    withDockerRegistry(credentialsId: 'dockerhub', toolName: 'docker') {
                        sh "docker push devops830/python-app:latest"
                    }
                }
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'image-report.html', fingerprint: true
        }
        failure {
            echo 'Pipeline failed. Please check the logs.'
        }
    }
}
