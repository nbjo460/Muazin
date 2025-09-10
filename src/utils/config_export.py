import os
from dotenv import load_dotenv

load_dotenv()

class General:
    WAV_FILES_PATH = os.getenv("WAV_FILES_PATH" ,r"C:\Users\Menachem\Desktop\Galil\Muazin\data\podcasts")
    FULL_PATH_KEY = "full_path"

class MetadataConfig:
    SIZE = "size"
    NAME = "name"
    CREATION_DATE = "creation date"
    LAST_MODIFICATION = "last modification"

class KafkaConfig:
    KAFKA_HOST = os.getenv("KAFKA_HOST", "localhost")
    KAFKA_PORT = os.getenv("KAFKA_PORT" ,"9092")

    FILE_DATA_TOPIC = os.getenv("FILE_DATA_TOPIC" ,"file_path_and_metadata")

class ElasticSearchConfig:
    ELASTIC_PORT = os.getenv("ELASTIC_PORT" ,"9200")
    ELASTIC_HOST = os.getenv("ELASTIC_HOST", "http://localhost:")
    ELASTIC_URL = ELASTIC_HOST + ELASTIC_PORT
    INDEX_NAME = os.getenv("INDEX_NAME" ,"podcasts")


class LoggingConfig:
    LOGGER_NAME = "Podcast_logger"
    INDEX_LOGS_NAME = "index_logs_name"

