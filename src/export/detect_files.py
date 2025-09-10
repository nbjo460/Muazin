from src.utils.config import General
from pathlib import Path

class DetectFiles:
    """
    Detecting files, and return the absolute path of each, in list
    """
    def __init__(self):
        self.podcasts_path = General.WAV_FILES_PATH

    def get_list_of_files(self) -> list:
        """
        return list of all podcasts path
        :return: list
        """
        abs_path = Path(self.podcasts_path).absolute()
        files_list = list(abs_path.iterdir())

        return files_list