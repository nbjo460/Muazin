from pathlib import Path
from config import MetadataConfig
from datetime import datetime

import config
import json

class Manager:
    def __init__(self):
        self.podcasts_path = config.WAV_FILES_PATH
    def run(self):
        self._control_metadata()

    def _control_metadata(self):
        podcasts_list = self._get_list_of_files()
        for podcast_path in podcasts_list:
            metadata = self._get_metadata_on_file(podcast_path)
            json_file_info = self._merge_metadata_and_path_to_json(metadata, podcast_path)
            print(json_file_info)


    def _merge_metadata_and_path_to_json(self, metadata : dict, file_path : Path):
        """
        :param metadata: the metadata of the file
        :param file_path: the path of the file
        :return: json
        """
        file_info = {str(file_path) : metadata}
        json_file_info = json.dumps(file_info)
        return json_file_info



    def _get_list_of_files(self) -> list:
        """
        return list of all podcasts path
        :return: list
        """
        podcasts_list = list(Path(self.podcasts_path).iterdir())
        return podcasts_list

    @staticmethod
    def _get_metadata_on_file(file_path : Path) -> dict:
        """
        return size, name, creation data, last modification date of file, as dictionary.
        :param file_path:  Path of file
        :return:
        """
        metadata = {}
        file_stat = file_path.stat()


        metadata[MetadataConfig.SIZE] = file_stat.st_size
        metadata[MetadataConfig.CREATION_DATE] = Manager._convert_timestamp_to_datetime(file_stat.st_ctime)
        metadata[MetadataConfig.LAST_MODIFICATION] = Manager._convert_timestamp_to_datetime(file_stat.st_mtime)
        metadata[MetadataConfig.NAME] = file_path.name

        return metadata

    @staticmethod
    def _convert_timestamp_to_datetime(timestamp):
        return str(datetime.fromtimestamp(timestamp))
