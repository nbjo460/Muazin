from src.utils.kafka_util.producer import Producer
from src.utils.config_export import KafkaConfig

class TransferData:
    def __init__(self):
        self.producer = Producer()

    def transfer_data(self, data: str) -> bool:
        """
        Transfer data by using Kafka. The Topic is decided in config file.
        :param data: data to transfer
        :return:  If the transfer succeed.
        """
        succeed = self.producer.publish_message(topic=KafkaConfig.FILE_DATA_TOPIC, message=data)
        return succeed
