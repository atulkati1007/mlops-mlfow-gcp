pipeline{
    agent any

    environment{
        VENV_DIR = "venv"
        GCP_PROJECT = "credstar-dataengg"
        GCLOUD_PATH = "/var/jenkins_home/google-cloud-sdk/bin"
        GCP_REGION = 'us-central1'  // Replace with your preferred region
        ARTIFACT_REPO = 'credstar-finops'  // Artifact Registry repository name
        IMAGE_NAME = 'mlops-project'  // Docker image name
        IMAGE_TAG = "${env.BUILD_ID}"  // Use Jenkins build ID as tag
        CLOUD_RUN_SERVICE = 'your-cloud-run-service'  // Cloud Run service name

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

        stage('Building and Pushing Docker Images to Goggle conatiner Regsitry'){
            steps{
                withCredentials([file(credentialsId: 'gcp-sa-key-file', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]){
                    script{
                        echo 'Buinding Docker image'
                        sh '''
                        gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}

                        gcloud config set project ${GCP_PROJECT}

                        gcloud auth configure-docker --quiet

                        docker build -t gcr.io${GCP_PROJECT}/${IMAGE_NAME}:latest .

                        docker push gcr.io${GCP_PROJECT}/${IMAGE_NAME}:latest
                        '''
                    }
                }
            }


        }
    }
}