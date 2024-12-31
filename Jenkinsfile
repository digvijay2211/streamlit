pipeline {
    agent any
    stages {
        stage("checkout code") {
            step {
                git url:"https://github.com/digvijay2211/streamlit.git",
                branch: "main"
            }
        }
    }
}