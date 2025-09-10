from src.utils.logger import Logger
from src.retriever.process.stt import Stt
from src.retriever.process.classified import Classified
from src.utils.config_retriever import DataRetrieverConfig, General
import shortuuid
import uuid
import json

class Processor:
    """
        Process metadata by:
        1. Add transcript.
        2. Classified dangerous
        Join to original data.

    """
    def __init__(self):
        self.logger = Logger().get_logger()
        self.stt = Stt()
        self.classified = Classified()

    def process_data(self, metadata : str) -> dict:
        """

        :param metadata: metadata of file.
        :param file_path: path of file.
        :return: metadata as dict, with transcript, and dangerous info.
        """

        metadata_dict = self._convert_to_dict(metadata)
        transcript = self._transcript(metadata_dict[General.FULL_PATH_KEY])
        bds_dict = self.classified.classified(transcript)
        processed_metadata = self._join_data(metadata_dict, bds_dict, transcript)

        return processed_metadata



    def _transcript(self, full_path : str):
        transcript =  self.stt.transcription(full_path)
        return transcript

    @staticmethod
    def _join_data(metadata : dict, bds_dict : dict, transcript : str) -> dict:
        metadata[DataRetrieverConfig.TRANSCRIPT] = transcript
        joined_metadata = metadata | bds_dict
        return joined_metadata

    @staticmethod
    def _convert_to_dict(message):
        return json.loads(message)

    @staticmethod
    def generate_id(metadata : str):
        """

        :param metadata: metadata of file
        :return: short unique id, based on metadata.
        """
        metadata = metadata.encode('utf-8')
        namespace_dns_uuid = uuid.NAMESPACE_DNS
        uuid_v5 = uuid.uuid5(namespace_dns_uuid, metadata)
        _id = shortuuid.encode(uuid_v5)
        return _id
