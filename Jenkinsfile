pipeline{
        agent any
        environment{
            DATABASE_URI = credentials("DATABASE_URI")
        }
        stages{
            stage('Build'){
                steps {
                    sh 'bash scripts/build.sh'
                }
            }
            stage('Push'){
                steps {
                    sh 'bash scripts/push.sh'
                }
            }
            stage('Configure'){
                steps {
                    sh 'bash scripts/configure.sh'
                }
            }         
        }
    }

chmod+x
// TEST - BUILD - PUSH - CONFIGURE - DEPLOY