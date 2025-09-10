from src.utils.mongo.dal import DAL as mongo_dal
from src.utils.elasticsearch_util.dal import DAL as es_DAL
from src.utils.logger import Logger
from src.utils.kafka_util import consumer

from src.utils.config_retriever import General
class UploadData:
    """
    Upload to metadata and audio files to servers.
    """
    def __init__(self):
        self.logger = Logger().get_logger()
        self.consumer = consumer.Consumer()
        self.elastic_dal = es_DAL()
        self.mongo_dal = mongo_dal()

    def upload_data(self, metadata : dict, _id_file : str):
        """
        Upload metadata to Elastic, and audios to Mongo.
        :param metadata:
        :param _id_file:
        :return:
        """
        self.elastic_dal.insert_podcast_data(_id_file, metadata)
        self.mongo_dal.upload_file(metadata[General.FULL_PATH_KEY], _id_file)
