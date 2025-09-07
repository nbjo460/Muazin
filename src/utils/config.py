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