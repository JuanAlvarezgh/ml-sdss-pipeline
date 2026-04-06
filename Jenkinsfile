pipeline {
    agent {
        docker {
            image 'python:3.11-slim'
            args '--user root'
        }
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Descargando codigo del repositorio...'
                checkout scm
            }
        }

        stage('Instalar dependencias') {
            steps {
                echo 'Instalando librerias Python...'
                sh 'pip install -r requirements.txt'
                sh 'pip install pytest'
            }
        }

        stage('Pruebas del dataset') {
            steps {
                echo 'Corriendo pruebas...'
                sh 'python -m pytest tests/test_dataset.py -v'
            }
        }

        stage('Ejecutar pipeline ML') {
            steps {
                echo 'Ejecutando el pipeline ML...'
                sh 'python main.py'
            }
        }

        stage('Guardar resultados') {
            steps {
                echo 'Guardando metricas y graficas...'
                archiveArtifacts artifacts: 'outputs/**/*', fingerprint: true
            }
        }
    }

    post {
        success {
            echo 'Pipeline completado exitosamente!'
        }
        failure {
            echo 'Algo fallo. Revisa los logs.'
        }
    }
}