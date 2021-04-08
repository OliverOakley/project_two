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
                steps{
                    script{
                        docker.withRegistry('https://registry.hub.docker.com', 'docker_hub_credentials'){
                            image.push("${env.app_version}")
                        }
                    }
                }
            }
        }

    }


// TEST - BUILD - PUSH - CONFIGURE - DEPLOY