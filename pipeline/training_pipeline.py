import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.data_ingestion import DataIngestion
from src.data_preprocessing import DataProcessor
from src.model_training import ModelTraining
from src.logger import get_logger
from src.custom_exception import CustomException
from utils.common_functions import load_data, read_yaml
from config.paths_config import *
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

logger = get_logger(__name__)

if __name__ == "__main__":
    try:
        logger.info("Starting the training pipeline")

        logger.info("Data Ingestion started")
        data_ingestion = DataIngestion(read_yaml(CONFIG_PATH))
        data_ingestion.run()
        logger.info("Data ingestion completed")
        
        logger.info("Data Preprocessing started")
        data_preprocessing = DataProcessor(TRAIN_FILE_PATH, TEST_FILE_PATH, PROCESSED_DIR, CONFIG_PATH)
        data_preprocessing.process() 
        logger.info("Data Preprocessing completed")

        logger.info("Model Training started")
        model_training = ModelTraining(PROCESSED_TRAIN_DATA_PATH,PROCESSED_TEST_DATA_PATH,MODEL_OUTPUT_PATH)
        model_training.run()
        logger.info("Model Training completed")
    except Exception as e:
        logger.error(f"Error in training pipeline: {e}")
        raise CustomException("Failed to train the model", e)