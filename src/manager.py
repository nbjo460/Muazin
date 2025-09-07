from src.data_export import DataExport
from src.utils.kafka_util import consumer
from src.utils import config

class Manager:
    def __init__(self):
        self.podcasts_path = config.WAV_FILES_PATH
        self.data_retrieve = DataExport(self.podcasts_path)
        self.consumer = consumer.Consumer()

    def run(self):

        self.data_retrieve.create_metadata()
        self._get_data()


    def _get_data(self):
        self.consumer.listen_topic()

