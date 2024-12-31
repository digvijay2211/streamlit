pipeline {
    agent any
    stages {
        stage("checkout code") {
            steps {
                git url:"https://github.com/digvijay2211/streamlit.git",
                branch: "main"
            }
        }
        
        stage('build image'){
            steps{
                sh 'docker build -t myimg .'
            }
        }
        
        stage('Tag and Push Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    sh 'echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin'
                    sh 'docker tag myimage $DOCKER_USERNAME/myimage'
                    sh 'docker push $DOCKER_USERNAME/myimage'
                }
                   
            }
        }

    }
}