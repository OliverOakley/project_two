pipeline{
        agent any
        environment{
            DATABASE_URI = credentials("DATABASE_URI")
            app_version = 'v1'
        }
        stages{
            stage('Build'){
                steps {
                    sh 'docker-compose build'
                }
            }
            stage('Push'){
                steps {
                    sh 'docker-compose push'
                }
            }         
        }
    }


// TEST - BUILD - PUSH - CONFIGURE - DEPLOY