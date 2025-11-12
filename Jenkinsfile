pipeline {
    agent any

    tools {
        allure 'allure-2.29.0'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/yourusername/playwright-allure.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\activate && pip install -r requirements.txt'
                bat 'venv\\Scripts\\activate && playwright install chromium'
            }
        }

        stage('Run Playwright Tests') {
            steps {
                bat 'venv\\Scripts\\activate && pytest --alluredir=allure-results'
            }
        }

        stage('Allure Report') {
            steps {
                allure([
                    includeProperties: false,
                    jdk: '',
                    results: [[path: 'allure-results']]
                ])
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'allure-results/**', fingerprint: true
        }
        failure {
            echo '❌ Tests failed!'
        }
        success {
            echo '✅ All tests passed successfully!'
        }
    }
}
