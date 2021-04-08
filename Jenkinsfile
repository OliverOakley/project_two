pipeline{
        agent any
        environment{
            DATABASE_URI = credentials("DATABASE_URI")
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
            stage('NGINX Configure'){
                steps {
                    sh 'ansible-playbook -i inventory.yaml playbook.yaml'
                }
            }         
        }
    }


// TEST - BUILD - PUSH - CONFIGURE - DEPLOY