from src.retriever.data_retriever import DataRetriever
from src.retriever.fetching_data import FetchingData
from src.retriever.upload_data import UploadData
from src.utils.logger import Logger
from src.retriever.process.process import Processor

class Manager:
    """
    Getting data from Kafka.
    Process it, add id, transcript, classified dangerous, join to data.
    Upload metadata to elastic, and podcasts to mongo.
    """
    def __init__(self):
        self.data_retriever = DataRetriever()
        self.logger = Logger().get_logger()
        self.fetching_data = FetchingData()
        self.processor = Processor()
        self.upload_data = UploadData()


    def run(self):
        self.logger.info("Getting Data.")
        self._listen_messages()

    def _listen_messages(self):
        listener = True
        while listener:
            print("------------------------------------------------------")
            metadata = self.fetching_data.fetch()
            unique_id = self.processor.generate_id(metadata)
            precessed_metadata = self.processor.process_data(metadata)
            self.upload_data.upload_data(precessed_metadata, unique_id)




