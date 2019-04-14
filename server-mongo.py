from pymongo import MongoClient
from flask import Flask, request
import json

app = Flask(__name__)
client = MongoClient('mongodb://<user>:<password>@ds143614.mlab.com:43614/ddos-test')
database = client['ddos-test']
data = database['data']


@app.route('/')
def save():
    data.insert_one({"message": request.args['data']})
    return request.args['data']

@app.route('/check')
def check():
    return data.count_documents()

app.run(port='8080')