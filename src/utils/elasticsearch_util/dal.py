from src.utils.config import ElasticSearchConfig
from elasticsearch import Elasticsearch

from src.utils.logger import Logger


class DAL:
    def __init__(self):
        self.URL = ElasticSearchConfig.ELASTIC_URL
        self.INDEX = ElasticSearchConfig.INDEX_NAME
        self.logger = Logger.get_logger()

        self.es = None
        self._create_connection()

    def _create_connection(self):
        try:
            self.logger.info("Connecting to ElasticSearch")
            self.es = Elasticsearch(self.URL)
            self.logger.info("Connected to ElasticSearch")
        except Exception as e:
            self.logger.warning("Connection to MONGO Failed!!!")

    def insert_podcast_data(self, _id, podcast):
        if not self.es.indices.exists(index=self.INDEX):
            self.logger.info(f"Creating new index {self.INDEX}")
            self.es.indices.create(index=self.INDEX)
        self.logger.info("Metadata uploaded to elastic.")
        response = self.es.index(index=self.INDEX, id=_id, document=podcast)
        return response