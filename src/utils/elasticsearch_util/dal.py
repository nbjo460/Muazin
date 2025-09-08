from src.utils.config import ElasticSearchConfig
from elasticsearch import Elasticsearch
class DAL:
    def __init__(self):
        self.URL = ElasticSearchConfig.ELASTIC_URL
        self.INDEX = ElasticSearchConfig.INDEX_NAME

        self.es = Elasticsearch(self.URL)

    def insert_podcast_data(self, _id, podcast):
        if not self.es.indices.exists(index=self.INDEX):
            self.es.indices.create(index=self.INDEX)
        response = self.es.index(index=self.INDEX, id=_id, body=podcast)
        return response