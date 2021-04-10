pipeline{
        agent any
        environment{
            DATABASE_URI = credentials("DATABASE_URI")
        }
        stages{
            stage('Test'){
                steps {
                    sh 'bash scripts/test.sh'
                }
            }
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
            stage('Deploy'){
                steps {
                    sh 'bash scripts/deploy.sh'
                }
            }         
        }
    }