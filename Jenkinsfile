@Library('shared') _
pipeline {
    agent any

    environment {
        SCANNER_HOME = tool 'sonar-scanner'
        DOCKER_IMAGE = 'devops830/python-app:latest'
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
                        env.OWASP_DC_NVD_API_KEY = 'f12ed65b-c318-4cae-8ff3-5ae529ec38da'
                        owasp_dependency()
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

    post {
        always {
            archiveArtifacts artifacts: 'image-report.html', fingerprint: true
        }
        failure {
            echo 'Pipeline failed. Please check the logs.'
        }
    }
}
