from pathlib import Path
from src.utils.config import MetadataConfig, KafkaConfig, General
from datetime import datetime
from src.utils.kafka_util.producer import Producer
from src.utils.logger import Logger
import json


class DataExport:
    def __init__(self, podcasts_path : str):
        self.producer = Producer()
        self.podcasts_path = podcasts_path
        self.logger = Logger().get_logger()

    def create_metadata(self):
        podcasts_list = self._get_list_of_files()
        self.logger.info(f"Start sent {len(podcasts_list)} files")
        succeeded_sum = 0
        for podcast_path in podcasts_list:
            metadata = self._get_metadata_on_file(podcast_path)
            json_file_info = self._merge_metadata_and_path_to_json(metadata, Path(podcast_path).name)
            succeeded = self._sent_to_info_kafka(file_info=json_file_info)
            if succeeded: succeeded_sum += 1
        self.logger.info(f"Finish sent {succeeded_sum} files.")



    @staticmethod
    def _merge_metadata_and_path_to_json(metadata : dict, file_name:str):
        """
        :param metadata: the metadata of the file
        :return: json
        """
        metadata[General.FULL_PATH_KEY] = str(metadata[General.FULL_PATH_KEY])
        boolshit = {file_name: metadata}
        json_file_info = json.dumps(metadata)
        return json_file_info

    def _get_list_of_files(self) -> list:
        """
        return list of all podcasts path
        :return: list
        """
        podcasts_list = list(Path(self.podcasts_path).iterdir())
        return podcasts_list

    def _sent_to_info_kafka(self, file_info : json):
        succeed = self.producer.publish_message(topic=KafkaConfig.FILE_DATA_TOPIC, message=file_info)
        return succeed

    def _get_metadata_on_file(self, file_path : Path) -> dict:
        """
        return size, name, creation data, last modification date of file, as dictionary.
        :param file_path:  Path of file
        :return:
        """
        metadata = {}
        file_stat = file_path.stat()

        metadata[General.FULL_PATH_KEY] = file_path
        metadata[MetadataConfig.SIZE] = file_stat.st_size
        metadata[MetadataConfig.CREATION_DATE] = self._convert_timestamp_to_datetime(file_stat.st_ctime)
        metadata[MetadataConfig.LAST_MODIFICATION] = self._convert_timestamp_to_datetime(file_stat.st_mtime)
        metadata[MetadataConfig.NAME] = file_path.name

        return metadata

    @staticmethod
    def _convert_timestamp_to_datetime(timestamp):
        return str(datetime.fromtimestamp(timestamp))
