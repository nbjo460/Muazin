import os
from dotenv import load_dotenv

load_dotenv()

class General:
    SUCCESS = "Succeeded!!!"
    FAILED = "Failed!!!"
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

class Errors:
    NO_BROKER_CONNECTION = "No broker connection."
    NO_MONGO_CONNECTION = "No Mongo Connection."

class ElasticSearchConfig:
    ELASTIC_PORT = os.getenv("ELASTIC_PORT" ,"9200")
    ELASTIC_HOST = os.getenv("ELASTIC_HOST", "http://localhost:")
    ELASTIC_URL = ELASTIC_HOST + ELASTIC_PORT
    INDEX_NAME = os.getenv("INDEX_NAME" ,"podcasts")

class MongoDBConfig:
    MONGO_HOST = os.getenv("MONGO_HOST" ,"localhost")
    MONGO_PORT = os.getenv("MONGO_PORT", "27017")
    MONGO_USER_NAME = os.getenv("MONGO_USER_NAME" ,None)
    MONGO_PASSWORD = os.getenv("MONGO_PASSWORD" ,None)
    MONGO_IS_ATLAS = os.getenv("MONGO_IS_ATLAS" ,"False")
    MONGO_PREFIX = os.getenv("MONGO_PREFIX", "mongodb+srv" if MONGO_IS_ATLAS == "True" else "mongodb")
    MONGO_DB_NAME = os.getenv("MONGO_DB_NAME" ,"Podcasts")

class LoggingConfig:
    LOGGER_NAME = "Podcast_logger"
    INDEX_LOGS_NAME = "index_logs_name"

class SttConfig:
    MODEL_PATH = os.getenv("MODEL_PATH", r"C:\Users\Menachem\Desktop\Galil\Muazin\data\model\vosk-model-small-en-us-0.15")

class DataRetrieverConfig:
    TRANSCRIPT = "transcript"

class ClassifiedConfig:
    HOSTILE_WORDS = "R2Vub2NpZGUsV2FyIENyaW1lcyxBcGFydGhlaWQsTWFzc2FjcmUsTmFrYmEsRGlzcGxhY2VtZW50LEh1bWFuaXRhcmlhbiBDcmlzaXMsQmxvY2thZGUsT2NjdXBhdGlvbixSZWZ1Z2VlcyxJQ0MsQkRT"
    LESS_HOSTILE_WORDS = "RnJlZWRvbSBGbG90aWxsYSxSZXNpc3RhbmNlLExpYmVyYXRpb24sRnJlZSBQYWxlc3RpbmUsR2F6YSxDZWFzZWZpcmUsUHJvdGVzdCxVTlJXQQ=="