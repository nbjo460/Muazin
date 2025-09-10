from src.utils.kafka_util import consumer
import uuid
import shortuuid
import json
from src.utils.elasticsearch_util.dal import DAL as es_DAL
from src.utils.mongo.dal import DAL as mongo_dal
from src.utils.logger import Logger
from stt import Stt
from src.utils.config import DataRetrieverConfig, General
from src.process.classified import Classified

class DataRetriever:
    def __init__(self):
        self.logger = Logger().get_logger()
        self.consumer = consumer.Consumer()
        self.stt = Stt()
        self.elastic_dal = es_DAL()
        self.mongo_dal = mongo_dal()
        self.classified = Classified()

    def store_data(self):
        podcasts_metadata = self.consumer.listen_topic()
        listener = True
        while listener:
            print("----------------------------------------------")
            podcast_metadata = next(podcasts_metadata)
            file_path, podcast_id, podcast_metadata_dict = self._extract_data(podcast_metadata)
            edited_metadata = self._add_transcription_to_metadata(podcast_metadata_dict, file_path)
            expanded_metadata = self._expand_metadata_by_bds(edited_metadata)
            self._store_data_to_dbs(file_path, podcast_id ,expanded_metadata)

    def _expand_metadata_by_bds(self, metadata : dict):
        text_bds = metadata[DataRetrieverConfig.TRANSCRIPT]
        bds_dict = self.classified.classified(text_bds)
        expanded_metadata = metadata | bds_dict
        return expanded_metadata

    def _store_data_to_dbs(self, file_path : str, podcast_id : str, podcast_metadata_dict : dict):
        self.elastic_dal.insert_podcast_data(podcast_id, podcast_metadata_dict)
        self.mongo_dal.upload_file(file_path, podcast_id)

    def _extract_data(self, _podcast_metadata):
        podcast_id = self._generate_unique_id(_podcast_metadata)
        podcast_metadata_dict = self.convert_to_dict(_podcast_metadata)
        file_path = podcast_metadata_dict[General.FULL_PATH_KEY]
        return file_path, podcast_id, podcast_metadata_dict

    def _add_transcription_to_metadata(self, metadata : dict, full_path : str):
        transcript =  self.stt.transcription(full_path)
        metadata[DataRetrieverConfig.TRANSCRIPT] = transcript
        return metadata


    @staticmethod
    def _generate_unique_id(message):
        message = message.encode('utf-8')
        namespace_dns_uuid = uuid.NAMESPACE_DNS
        uuid_v5 = uuid.uuid5(namespace_dns_uuid, message)
        _id = shortuuid.encode(uuid_v5)
        return _id


    @staticmethod
    def convert_to_dict(message):
        return json.loads(message)


if __name__ == "__main__":
    def clean_kafka():
        consumer1 = consumer.Consumer()
        podcasts_metadata = consumer1.listen_topic()
        listener = True
        while listener:
            podcast_metadata = next(podcasts_metadata)
            print("CLAEN" + podcast_metadata)
    def clean_es():
        es = es_DAL()
        return es.delete_index()
    print(clean_es())
    clean_kafka()
