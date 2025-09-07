from src.utils.kafka_util import consumer
import hashlib

class DataRetriever:
    def __init__(self):
        self.consumer = consumer.Consumer()

    def store_data(self):
        listener = True
        messages = self.consumer.listen_topic()
        while listener:
            message = next(messages)
            message = message.encode('utf-8')
            hash_id = self._generate_unique_id(message)

    @staticmethod
    def _generate_unique_id(message):
        hasher = hashlib.sha256()
        hasher.update(message)
        return hasher.hexdigest()

