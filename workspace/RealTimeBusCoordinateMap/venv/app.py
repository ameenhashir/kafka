from flask import Flask,Response,render_template
from kafka import KafkaConsumer
import json

app = Flask(__name__)

@app.route('/')
def index():
    return(render_template('index.html'))

#consumer API
@app.route('/topic/<topicname>')
def get_message(topicname):
    data =''
    consumer = KafkaConsumer(topicname,
                             bootstrap_servers=['192.168.1.112:9092'],
                             auto_offset_reset ='latest',
                             group_id='buslines')
    def event():
        for msg in consumer:
             #data = '{0}'.format(json.loads(msg.value.decode()))
             data = 'data:{0}\n\n'.format(msg.value.decode())
             yield data
    return Response(event(),mimetype="text/event-stream")

if __name__ == '__main__':
    app.run(debug=True,port=5001)