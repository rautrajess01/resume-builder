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
        withCredentials([file(credentialsId: 'f435a460-5a39-4218-ac61-92c824680b73', variable: 'ENV_FILE')]){
        sh '''
        cat $ENV_FILE >> .env
        docker compose up -d  --build
        '''
        }
      }
    }
    stage('Run A Migration') {
      steps{
        sh '''
        docker compose exec web python manage.py makemigrations builder
        docker compose exec web python manage.py migrate
        '''
      }
    }
  }

}
