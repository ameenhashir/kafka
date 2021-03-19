import kafka as k
import json
from data import get_registered_user
import time

def data_serializer(data):
    return json.dumps(data).encode('utf-8')

def get_partition(keybytes,allpartition,availablepartition):
    return 0

#producer = k.KafkaProducer(bootstrap_servers=['10.145.21.36:9092'],value_serializer=data_serializer)
#send to particular partition
producer = k.KafkaProducer(bootstrap_servers=['10.145.21.36:9092'],value_serializer=data_serializer,partitioner=get_partition)


if __name__ == '__main__':
    while True:
        data = get_registered_user()
        print(data_serializer(data))
        producer.send('registered_user',data)
        time.sleep(5)