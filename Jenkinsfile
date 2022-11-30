pipeline {
    agent { label 'jenkins-agent' } 
    stages {
       stage('build docker image') {
        steps {
                 sh 'docker build -t emailscrapy .' 
            }
       }
       stage("remove unused image"){
            steps{
              sh 'docker image prune -a -f'  
            }
        }
    }   
}