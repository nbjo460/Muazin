WAV_FILES_PATH = r"C:\Users\Menachem\Desktop\Galil\Muazin\data\podcasts"

class MetadataConfig:
    SIZE = "size"
    NAME = "name"
    CREATION_DATE = "creation date"
    LAST_MODIFICATION = "last modification"

class KafkaConfig:
    KAFKA_HOST = "localhost"
    KAFKA_PORT = "9092"

    FILE_DATA_TOPIC = "file_path_and_metadata"

class Errors:
    NO_BROKER_CONNECTION = "No broker connection."

class ElasticSearchConfig:
    ELASTIC_PORT = "9200"
    ELASTIC_HOST = "http://localhost:"
    ELASTIC_URL = ELASTIC_HOST + ELASTIC_PORT
    INDEX_NAME = "podcasts"
class MongoDBConfig:
    HOST = "localhost"
    PORT = "27017"
    USER_NAME = None
    PASSWORD = None
    IS_ATLAS = False
    PREFIX = "mongodb+srv" if IS_ATLAS else "mongodb"
    DB_NAME = "Podcasts"