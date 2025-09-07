from pathlib import Path
from config import MetadataConfig
import config

class Manager:
    def __init__(self):
        self.podcasts_path = config.WAV_FILES_PATH
    def run(self):
        self._control_metadata()

    def _control_metadata(self):
        podcasts_list = self._get_list_of_files()
        for podcast in podcasts_list:
            self._get_metadata_on_file(podcast)



    def _get_list_of_files(self):
        """
        return list of all podcasts path
        :return: list
        """
        podcasts_list = list(Path(self.podcasts_path).iterdir())
        return podcasts_list

    @staticmethod
    def _get_metadata_on_file(file_path : Path):
        """
        return size, name, creation data, last modification date of file, as dictionary.
        :param file_path:  Path of file
        :return:
        """
        metadata = {}
        file_stat = file_path.stat()
        metadata[MetadataConfig.SIZE] = file_stat.st_size
        metadata[MetadataConfig.CREATION_DATE] = file_stat.st_ctime
        metadata[MetadataConfig.LAST_MODIFICATION] = file_stat.st_mtime
        metadata[MetadataConfig.NAME] = file_path.name

        return metadata

