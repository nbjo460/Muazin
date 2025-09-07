"""
This file contains the sample code which publishes message to the Kafka brokers.

1. publish_message function pushes the message to the topic
2. publish_message_with_key pushes the message with key

"""

# Import all the required packages
import json
from kafka import KafkaProducer, errors
from src.config import KafkaConfig, Errors
from src.exception import NoBrokerConnection


def get_producer_config():
    # The Producer object requires the Kafka server, Json serializer
    url = f'{KafkaConfig.KAFKA_HOST}:{KafkaConfig.KAFKA_PORT}'
    try:
        produce = KafkaProducer(bootstrap_servers=[url],
                             value_serializer=lambda x:
                             json.dumps(x).encode('utf-8'))
    except errors.NoBrokersAvailable as e:
        produce = Errors.NO_BROKER_CONNECTION
        print(e, "Can't connect to Kafka server")
    return produce

# Publish json messages
def publish_message(producer, topic, message) -> str:
    """
    This function will publish message to the topic which is received as a parameter
    :param producer: producer object to publish the message to Kafka servers
    :param topic: The topic to which the message will be published
    :param message: The event message
    :return: None
    """

    try:
        if producer == Errors.NO_BROKER_CONNECTION:
            raise NoBrokerConnection
        producer.send(topic, message)
        producer.flush()
        return "Success!!"
    except NoBrokerConnection as e:
        print(e)



if __name__ == '__main__':

    # Create the producer object with basic configurations
    producer = get_producer_config()

    #Publish message to a topic

    #Publish message to a topic with key to enable hashed partitioning
    publish_message(get_producer_config(),"topic1",b"client1")

    # block until all async messages are sent
    producer.flush()