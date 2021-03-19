from kafka import KafkaConsumer
import json


if __name__ == '__main__':
    consumer = KafkaConsumer('track_bus',
                             bootstrap_servers=['10.152.21.177:9092'],
                             auto_offset_reset = 'earliest',
                             group_id='buslines')

    for msg in consumer:
        print(json.loads(msg.value))