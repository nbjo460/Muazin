from pathlib import Path
from src.utils.config import MetadataConfig, General
from datetime import datetime
from src.utils.logger import Logger
import json


class ExtractMetadata:
    """
    Extracting metadata of file, as str (converted from dict).
    """
    def __init__(self):
        self.logger = Logger().get_logger()

    def create_metadata(self, file_path) -> str:
        """

        :param file_path: absolute path of file.
        :return: converted dict (to string) of metadata.
        """
        metadata = self._get_metadata_on_file(file_path)
        json_file_info = self._merge_metadata_and_path_to_json(metadata)
        return json_file_info


    @staticmethod
    def _merge_metadata_and_path_to_json(metadata : dict):
        """
        :param metadata: the metadata of the file
        :return: json
        """
        metadata[General.FULL_PATH_KEY] = str(metadata[General.FULL_PATH_KEY])
        json_file_info = json.dumps(metadata)
        return json_file_info


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
