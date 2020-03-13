import os

from flask import Flask,request
import json
from flask import flash

def create_app(test_config=None):
    #create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE = os.path.join(app.instance_path,'flaskr.sqlite')
    )

    # A simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    
    @app.route('/posttokafka',methods=["GET","POST"])
    def posttokafka():
        if request.method == "POST":
            note = request.json
            return note

        return OK
    
    #verify the data you are posting by hitting this api
    @app.route('/example')
    def example():
        return {'request data': request.data}
    
    return app