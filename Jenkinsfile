pipeline{
        agent any
        environment{
            DATABASE_URI = credentials("DATABASE_URI")
        }
        stages{
            stage('Build'){
                steps {
                    sh "./scripts/build.sh"
                }
            }
            stage('Push'){
                steps {
                    sh "./scripts/push.sh"
                }
            }
            stage('Configure'){
                steps {
                    sh "./scripts/configure.sh"
                }
            }         
        }
    }


// TEST - BUILD - PUSH - CONFIGURE - DEPLOY