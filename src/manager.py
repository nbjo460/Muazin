import threading
from threading import Thread

from src.data_export import DataExport
from src.data_retriever import DataRetriever
from src.utils import config

class Manager:
    def __init__(self):
        self.podcasts_path = config.WAV_FILES_PATH
        self.data_export = DataExport(self.podcasts_path)
        self.data_retriever = DataRetriever()

    def run(self):
        create_data = self.data_export.create_metadata()
        storing_data = threading.Thread(target=self.data_retriever.store_data)

        storing_data.start()

