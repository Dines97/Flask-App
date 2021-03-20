import os

import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

url = os.getenv('WEBHOOK_URL')
data = {'firstname': None,
        'lastname': None}


@app.route('/', methods=['GET'])
def home():
    return "My name is Denis Kaynar"


@app.route('/whoami', methods=['GET'])
def whoami():
    data["firstname"] = request.args.get('firstname')
    data["lastname"] = request.args.get('lastname')
    return jsonify(data)


@app.route('/alert', methods=['POST'])
def alert():
    if request.is_json:
        requests.post(url, headers={'Content-Type': 'application/json'}, json=request.get_json())
    else:
        return 'Bad Request', 400


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
