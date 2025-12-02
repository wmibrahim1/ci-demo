pipeline {
  agent {
    docker {
      image 'python:3.11-slim'
      args '-u root:root'   // run as root so we can install deps
    }
  }
  environment {
    WEBEX_BOT_TOKEN = credentials('OWYwYjk4ZTktMjQ0MC00YTE2LWI3M2EtOTBhMGU5ODUwNGZlMDg5MGYwYjMtZTM0_P0A1_13494cac-24b4-4f89-8247-193cc92a7636') // store token in Jenkins credentials
    WEBEX_ROOM_ID  = credentials('8c279730-c9af-11f0-8763-8bd6607adee2')    // store target roomId (or use plain string)
  }
  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }
    stage('Install deps') {
      steps {
        sh 'python -m pip install --upgrade pip'
        sh 'pip install -r requirements.txt'
      }
    }
    stage('Run tests') {
      steps {
        sh 'pytest --junitxml=reports/results.xml'
        junit 'reports/results.xml'
      }
    }
  }
  post {
    success {
      script {
        def msg = "✅ Jenkins Build SUCCESS: Job ${env.JOB_NAME} #${env.BUILD_NUMBER} (${env.BUILD_URL})"
        sh """
          curl -s -X POST https://webexapis.com/v1/messages \
            -H "Authorization: Bearer ${WEBEX_BOT_TOKEN}" \
            -H "Content-Type: application/json" \
            -d '{"roomId":"${WEBEX_ROOM_ID}","markdown":"${msg}"}'
        """
      }
    }
    failure {
      script {
        def msg = "❌ Jenkins Build FAILED: Job ${env.JOB_NAME} #${env.BUILD_NUMBER} (${env.BUILD_URL})"
        sh """
          curl -s -X POST https://webexapis.com/v1/messages \
            -H "Authorization: Bearer ${WEBEX_BOT_TOKEN}" \
            -H "Content-Type: application/json" \
            -d '{"roomId":"${WEBEX_ROOM_ID}","markdown":"${msg}"}'
        """
      }
    }
  }
}
