pipeline{
        agent any
        environment{
            DATABASE_URI = credentials("DATABASE_URI")
        }
        stages{
            stage('Build'){
                steps {
                    sh chmod +x "./scripts/build.sh"
                }
            }
            stage('Push'){
                steps {
                    sh chmod +x "./scripts/push.sh"
                }
            }
            stage('Configure'){
                steps {
                    sh chmod +x "./scripts/configure.sh"
                }
            }         
        }
    }


// TEST - BUILD - PUSH - CONFIGURE - DEPLOY