pipeline{
    agent any

    stages{
        stage('Cloning Github repo to jenkins workspace') {
            steps{
                script{
                    echo 'Cloning Github repo to jenkins workspace'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/atulkati1007/mlops-mlfow-gcp.git']])
                }
            }
       }
    }
}