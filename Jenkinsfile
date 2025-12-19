pipeline{
    agent any

    environment{
        VENV_DIR = "venv"
    }

    stages{
        stage('Cloning Github repo to jenkins workspace') {
            steps{
                script{
                    echo 'Cloning Github repo to jenkins workspace'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/atulkati1007/mlops-mlfow-gcp.git']])
                    }
                }
            }
        stage('Create python vritual environment'){
            steps{
                script{
                    echo "Creating python vitual environment"
                    sh '''
                    # Install Python dependencies
                    python -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    '''
                    echo "Virtual Environment has been created"
                }
            }
        }
    }
}