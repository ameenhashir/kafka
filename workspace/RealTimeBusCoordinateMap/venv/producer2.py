from kafka import KafkaProducer
import json
import uuid
from datetime import datetime
import time

#kafka Producer
def get_serializer(data):
    return json.dumps(data).encode('utf-8')

producer = KafkaProducer(bootstrap_servers=['10.152.21.186:9092'],value_serializer=get_serializer)

#uid
def generate_uuid(busline):
    return busline + '_' + str(uuid.uuid4())

#read bus co-ordinates
with open('./data/bus2.json','r') as fn:
     bus_data = json.load(fn)
coordinates=bus_data['features'][0]['geometry']['coordinates']

data = {}
data['busline'] = '0002'

def generate_coordinates(coordinates):
    i=0
    while True:
        data['key'] = generate_uuid(data['busline'])
        data['timestamp'] = str(datetime.utcnow())
        data['longitude'] = coordinates[i][0]
        data['latitude'] = coordinates[i][1]
        #send to kafka
        producer.send('track_bus',data)
        #continous loop
        if i < len(coordinates)-1:
            i+=1
        else:
            i=0
        print(data)
        time.sleep(1)



generate_coordinates(coordinates)

