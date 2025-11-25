pipeline {
    agent {
        docker { image 'python:3.11-slim' }
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/wmibrahim1/ci-demo.git', credentialsId: 'github-creds'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest'
            }
        }
    }

    post {
        success {
            script { sendWebexMessage("✅ Build SUCCESS for ${env.JOB_NAME} #${env.BUILD_NUMBER}") }
        }
        failure {
            script { sendWebexMessage("❌ Build FAILED for ${env.JOB_NAME} #${env.BUILD_NUMBER}") }
        }
    }
}

def sendWebexMessage(String messageText) {
    withCredentials([string(credentialsId: 'webex_bot_token', variable: 'WEBEX_TOKEN')]) {
        sh """
        curl -X POST \
             -H "Authorization: Bearer $WEBEX_TOKEN" \
             -H "Content-Type: application/json" \
             -d '{ "roomId": "aHR0cHM6Ly9jb252LXIud2J4Mi5jb20vY29udmVyc2F0aW9uL2FwaS92MS9jb252ZXJzYXRpb25zLzhjMjc5NzMwLWM5YWYtMTFmMC04NzYzLThiZDY2MDdhZGVlMg", "text": "${messageText}" }' \
             https://webexapis.com/v1/messages
        """
    }
}
