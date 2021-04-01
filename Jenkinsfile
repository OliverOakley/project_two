pipeline{
        agent any
        stages{
            stage('test'){
                steps {
                    echo "test"

                }
            }
        }
        post { 
            always { 
                cleanWs()
                }
            }
}
