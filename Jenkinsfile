pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'YOUR_REPO_URL'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
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
            script {
                sendWebexMessage("✅ Build SUCCESS for ${env.JOB_NAME} #${env.BUILD_NUMBER}")
            }
        }
        failure {
            script {
                sendWebexMessage("❌ Build FAILED for ${env.JOB_NAME} #${env.BUILD_NUMBER}")
            }
        }
    }
}

def sendWebexMessage(String messageText) {
    withCredentials([string(credentialsId: 'webex_bot_token', variable: 'WEBEX_TOKEN')]) {
        sh """
            curl -X POST \
                 -H "Authorization: Bearer $WEBEX_TOKEN" \
                 -H "Content-Type: application/json" \
                 -d '{ "roomId": "YOUR_ROOM_ID_HERE", "text": "${messageText}" }' \
                 https://webexapis.com/v1/messages
        """
    }
}

