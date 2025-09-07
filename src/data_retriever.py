from src.utils.kafka_util import consumer
import hashlib
import json
from src.utils.elasticsearch_util.dal import DAL as es_DAL

class DataRetriever:
    def __init__(self):
        self.consumer = consumer.Consumer()
        self.elastic_dal = es_DAL()

    def store_data(self):
        listener = True
        messages = self.consumer.listen_topic()
        while listener:
            message = next(messages)
            hash_id = self._generate_unique_id(message)
            message = self.convert_to_json(message)
            self.elastic_dal.insert_podcast_data(hash_id ,message)


    @staticmethod
    def _generate_unique_id(message):
        message = message.encode('utf-8')
        hasher = hashlib.sha256()
        hasher.update(message)
        return hasher.hexdigest()

    @staticmethod
    def convert_to_json(message):
        return json.loads(message)

