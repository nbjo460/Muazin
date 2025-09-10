import threading

from src.export.data_export import DataExport
from src.data_retriever import DataRetriever
from src.utils import config
from src.utils.logger import Logger

class Manager:
    def __init__(self):
        self.podcasts_path = config.General.WAV_FILES_PATH
        self.data_export = DataExport(self.podcasts_path)
        self.data_retriever = DataRetriever()
        self.logger = Logger().get_logger()


    def run(self):
        self.logger.info("Exporting MetaData.")
        create_data = self.data_export.create_metadata()
        storing_data = threading.Thread(target=self.data_retriever.store_data)

        self.logger.info("Getting Data, Thread opened.")
        storing_data.start()

