pipeline{
        agent any
        environment{
            DATABASE_URI = credentials("DATABASE_URI")
        }
        stages{
            stage('Build'){
                steps {
                    chmod +x sh "./scripts/build.sh"
                }
            }
            stage('Push'){
                steps {
                    chmod +x sh"./scripts/push.sh"
                }
            }
            stage('Configure'){
                steps {
                    chmod +x sh "./scripts/configure.sh"
                }
            }         
        }
    }


// TEST - BUILD - PUSH - CONFIGURE - DEPLOY