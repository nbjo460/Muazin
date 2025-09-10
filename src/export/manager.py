from src.export.extract_metadata import ExtractMetadata
from src.export.transfer_data import TransferData
from src.export.detect_files import DetectFiles
from src.utils.logger import Logger

class Manager:
    """
    Extract Metadata from all files, and send them.
    """
    def __init__(self):
        self.detect_files = DetectFiles()
        self.extract_metadata = ExtractMetadata()
        self.transfer_data = TransferData()
        self.logger = Logger().get_logger()


    def run(self):
        self.logger.info("Detecting files.")
        podcasts_path = self.detect_files.get_list_of_files()
        self._run_each_file(podcasts_path)

    def _run_each_file(self, podcasts_paths):
        """
        Send metadata of each file.
        Log how many succeed.
        :param podcasts_paths: Path of the podcasts files.
        :return: None
        """
        self.logger.info("Export and send MetaData.")
        succeed = 0
        for podcast in podcasts_paths:
            metadata = self.extract_metadata.create_metadata(podcast)
            is_succeed = self.transfer_data.transfer_data(metadata)
            succeed += 1 if is_succeed else 0
        self.logger.info(f"Transfer {succeed} podcasts metadata.")


