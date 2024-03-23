from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, methods=["GET"])

animals = {
    'lion': 'The lion is a species in the family Felidae; it is a muscular, deep-chested cat with a short, rounded head, a reduced neck, and round ears, and a hairy tuft at the end of its tail.',
    'elephant': 'Elephants are mammals of the family Elephantidae and the largest existing land animals.',
    'giraffe': 'The giraffe is an African artiodactyl mammal, the tallest living terrestrial animal and the largest ruminant.'
}

@app.route('/')
def home():
    return jsonify({'msg':'This is Home'})


@app.route('/testing', methods=['GET'])
def testing():
    return jsonify({'testing': 'Server Is Running!'})

@app.route('/animal/<string:name>', methods=['GET'])
def get_animal(name):
    if name in animals:
        return jsonify({'name': name, 'description': animals[name]})
    else:
        return jsonify({'error': 'Animal not found'}), 404

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
