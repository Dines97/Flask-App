from flask import Flask, request, jsonify

app = Flask(__name__)

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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
