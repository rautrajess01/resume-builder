pipeline {
  agent any

    // triggers {
    //     pollSCM('* * * * *')
    // }
  stages{
    stage('Checkout Code'){
      steps{

      git branch: 'main', url: 'https://github.com/rautrajess01/resume-builder.git'

      }
    }
    stage('Run A Compose File'){
      steps {
        withCredentials([file(credentialsId: '54bf3e26-cc62-4356-877a-b776be8f27f3', variable: 'ENV_FILE')]){
        sh '''
        cat $ENV_FILE >> .env
        docker compose up -d  --build
        '''
        }
      }
    }
    stage('Run A Migration') {
      steps{
        sh 'docker compose exec web python manage.py migrate'
      }
    }
  }

}
