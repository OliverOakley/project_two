pipeline{
        agent any
        stages{
            stage('Clear'){
                steps{
                    sh "touch ~/jenkins-tutorial-test/file1 ~/jenkins-tutorial-test/file2"
            stage('Make Directory'){
                steps{
                    sh "mkdir ~/jenkins-tutorial-test"
                }
            }
            post { 
                always { 
                    cleanWs()
                }
            }
        }
}
