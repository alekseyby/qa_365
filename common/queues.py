from confluent_kafka import Consumer, TopicPartition


class QueueClass:
    """Base class to work with Kafka, contains method to create Consumer and get amount of messages in topic
    """
    def __init__(self, host, port):
        self.bootstrap_server = f'{host}:{port}'
        self.topic = None
        self.npartitions = None
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
