from kafka import KafkaConsumer
from src.utils.config import KafkaConfig
import json

class Consumer:
    def __init__(self):
        self.TOPIC = KafkaConfig.FILE_DATA_TOPIC
        self.consumer = None

    def get_consumer_events(self):
        # The consumer object contains the topic name, json deserializer,Kafka servers
        # and kafka time out in ms, Stops the iteration if no message after 1 sec
        self.consumer = KafkaConsumer(self.TOPIC,
                                 group_id='my-group',
                                 value_deserializer=lambda m: json.loads(m.decode('utf-8')),
                                 bootstrap_servers=[f'{KafkaConfig.KAFKA_HOST}:{KafkaConfig.KAFKA_PORT}']
                                 )
        return self.consumer


    def processor_messages(self):
        # Iterate through the messages
        if self.consumer is not None:
            for message in self.consumer:
                print(message.offset, message.value)
                yield  message.value


    def listen_topic(self):
        print(f"listen to {self.TOPIC} messages")
        #Create consumer object which consumes any message from the topic

        self.get_consumer_events()
        messages = self.processor_messages()
        message = next(messages)
        print(message)
        return message

