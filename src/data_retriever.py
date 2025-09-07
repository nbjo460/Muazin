from src.utils.kafka_util import consumer

class DataRetriever:
    def __init__(self):
        self.consumer = consumer.Consumer()

    def store_data(self):
        listener = True
        messages = self.consumer.listen_topic()
        while listener:
            message = next(messages)
            print(message)

