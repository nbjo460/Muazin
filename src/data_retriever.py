from src.utils.kafka_util import consumer
import uuid
import shortuuid
import json
from src.utils.elasticsearch_util.dal import DAL as es_DAL
from src.utils.mongo.dal import DAL as mongo_dal
from src.utils.logger import Logger

class DataRetriever:
    def __init__(self):
        self.consumer = consumer.Consumer()
        self.elastic_dal = es_DAL()
        self.mongo_dal = mongo_dal()
        self.logger = Logger().get_logger()

    def store_data(self):
        self.logger.info("Start listening")
        listener = True
        podcasts_metadata = self.consumer.listen_topic()
        while listener:
            podcast_metadata = next(podcasts_metadata)
            podcast_id = self._generate_unique_id(podcast_metadata)
            podcast_metadata_json = self.convert_to_json(podcast_metadata)
            self.elastic_dal.insert_podcast_data(podcast_id ,podcast_metadata_json)
            file_path = list(podcast_metadata_json.keys())[0]
            self.mongo_dal.upload_file(file_path, podcast_id)




    @staticmethod
    def _generate_unique_id(message):
        message = message.encode('utf-8')
        namespace_dns_uuid = uuid.NAMESPACE_DNS
        uuid_v5 = uuid.uuid5(namespace_dns_uuid, message)
        _id = shortuuid.encode(uuid_v5)
        return _id


    @staticmethod
    def convert_to_json(message):
        return json.loads(message)

