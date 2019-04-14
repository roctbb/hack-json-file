from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/')
def save():
    file = open('app.json', 'r')
    content = json.loads(file.read())
    file.close()

    content.append(request.args['data'])

    file = open('app.json', 'w')
    file.write(json.dumps(content))
    file.close()

    return request.args['data']

@app.route('/check')
def check():
    file = open('app.json', 'r')
    content = json.loads(file.read())
    file.close()

    return len(content)

app.run(port='8080')