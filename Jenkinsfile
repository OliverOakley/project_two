pipeline{
        agent any
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