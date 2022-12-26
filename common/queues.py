from confluent_kafka import Consumer, TopicPartition
from confluent_kafka.admin import AdminClient


class QueueClass:
    """Base class to work with Kafka, contains method to create Consumer and get amount of messages in topic
    """

    def __init__(self, host, port):
        self.bootstrap_server = '{}:{}'.format(host, port)
        self.admin = AdminClient({'bootstrap.servers': self.bootstrap_server, 'security.protocol': 'SASL_SSL',
                                  'sasl.mechanisms': 'PLAIN',
                                  'sasl.username': 'ADSD',
                                  'sasl.password': 'ADSD'
                                  })
        self.topic = 'kafka-test'
        self.npartitions = 5
        self.consumer = None

    def create_consumer(self, auto_offset_reset='earliest', group_id=''):
        """Creates consumer"""
        self.consumer = Consumer({'bootstrap.servers': self.bootstrap_server,
                                  'group.id': group_id,
                                  'default.topic.config': {'auto.offset.reset': auto_offset_reset}})
        return self.consumer

    def consume_msgs(self):
        """ Getting messages from topic"""
        messages = []
        for partition in range(0, self.npartitions):
            self.consumer.assign([TopicPartition(self.topic, partition)])
            while True:
                msg = self.consumer.poll(timeout=0.1)
                if msg is None:
                    continue
                if msg.error():
                    print(f'Consumer error happened: {msg.error()}')
                    continue
                print(f'Received Message : {msg.value()} with Offset : {msg.offset()}')
                messages.append(msg)
            self.consumer.close()
        return messages


test_queue = QueueClass('pkc-lq8v7.eu-central-1.aws.confluent.cloud', 9092)
test_queue.create_consumer(group_id='web-3ea22c97-d625-4bb2-ba91-e3c48d38378a')
messages = test_queue.consume_msgs()
