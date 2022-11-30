pipeline {
    agent { label 'jenkins-agent' } 
    stages {
       stage('build docker image') {
        steps {
                 sh 'docker build -t emailscrapy .' 
            }
       }
    }   
}