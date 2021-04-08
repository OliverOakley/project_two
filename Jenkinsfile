pipeline{
        agent any
        environment{
            DATABASE_URI = credentials("DATABASE_URI")
        }
        stages{
            stage('Build'){
                steps {
                    sh('build.sh')
                }
            }
            stage('Push'){
                steps {
                    sh ('push.sh')
                }
            }
            stage('Configure'){
                steps {
                    sh ('configure.sh')
                }
            }         
        }
    }


// TEST - BUILD - PUSH - CONFIGURE - DEPLOY