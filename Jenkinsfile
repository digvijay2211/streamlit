pipeline {
    agent any
    stages {
        stage("checkout code") {
            steps {
                git url:"https://github.com/digvijay2211/streamlit.git",
                branch: "main"
            }
        }
        stage('clean Up'){
            steps{
                sh 'docker rm -f $(docker ps -aq)'
            }
            
        }
        stage('build image'){
            steps{
                sh 'docker build -t myimg .'
            }
        }
        stage('create conatiner'){
            steps{
                sh 'docker run -d -p 8501:8501 myimg'
            }
        }
    }
}