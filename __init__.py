from flask import Flask,request
from kafka import KafkaProducer
import json
import os

def create_app():
    # create and configure the app
    app = Flask(__name__)

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.route('/posttokafka',methods=["POST"])
    def posttokafka():
        note = request.json
        #print(note)
        producer = producer = KafkaProducer(bootstrap_servers=['localhost:9092'],value_serializer=lambda m: json.dumps(m).encode('utf-8'))
        producer.send('quick_start',value=note)
        return 'OK'

    return app
