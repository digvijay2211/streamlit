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
        stage('create conatiner'){
            steps{
                sh 'docker apply -d -p 8501:8501 myimg'
            }
        }
    }
}