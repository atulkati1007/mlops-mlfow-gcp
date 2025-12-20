pipeline{
    agent any

    environment{
        VENV_DIR = "venv"
        GCP_PROJECT = "credstar-dataengg"
        GCLOUD_PATH = "/var/jenkins_home/google-cloud-sdk/bin"
        GCP_REGION = 'us-central1'  // Replace with your preferred region
        ARTIFACT_REPO = 'airflow-images'  // Artifact Registry repository name
        IMAGE_NAME = 'mlops-project'  // Docker image name
        IMAGE_TAG = "${env.BUILD_ID}"  // Use Jenkins build ID as tag
        CLOUD_RUN_SERVICE = 'credstar-mlops-project'  // Cloud Run service name

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

                        gcloud auth configure-docker ${GCP_REGION}-docker.pkg.dev

                        docker build -t ${GCP_REGION}-docker.pkg.dev/${GCP_PROJECT}/${ARTIFACT_REPO}/${IMAGE_NAME}:${IMAGE_TAG} .

                        docker push ${GCP_REGION}-docker.pkg.dev/${GCP_PROJECT}/${ARTIFACT_REPO}/${IMAGE_NAME}:${IMAGE_TAG}
                        '''
                    }
                }
            }
        }

        stage("Deploy to Google cloud run"){
            steps{
                withCredentials([file(credentialsId: 'gcp-sa-key-file', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]){
                    script{
                        echo "Dpploy to del=ploy to cloud run"
                        sh '''
                        gcloud auth activate-service-account --key-file=$GOOGLE_APPLICATION_CREDENTIALS

                        # Deploy to Cloud Run (creates service if not exists)
                        gcloud run deploy ${CLOUD_RUN_SERVICE} \
                            --image=${GCP_REGION}-docker.pkg.dev/${GCP_PROJECT}/${ARTIFACT_REPO}/${IMAGE_NAME}:${IMAGE_TAG} \
                            --platform=managed \
                            --region=${GCP_REGION} \
                            --allow-unauthenticated  # Allow public access; change as needed
                        '''
                    }
                }
            }
        }

    
    
    } //end of stages


       
} //end of pipeline