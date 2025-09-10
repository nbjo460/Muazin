from src.utils.logger import Logger
from src.utils.kafka_util import consumer

class FetchingData:
    """
    Fetching always data from kafka.
    """
    def __init__(self):
        self.consumer = consumer.Consumer()
        self.logger = Logger().get_logger()


    def fetch(self):
        """
        Metadata fetched by 'next'. Should call by 'while' loop.
        :return:  Metadata.
        """
        podcasts_metadata = self.consumer.listen_topic()
        metadata = next(podcasts_metadata)
        return metadata


