from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 
app.config['MONGO_URI'] = 'mongodb://mongodb:27017/db'
mongo = PyMongo(app)

@app.route('/submit', methods=['POST'])
def submit_form():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    if name and email:
        db = mongo.db.users
        db.insert_one({'name': name, 'email': email})
        
        return jsonify({'message': 'Data inserted successfully'}), 201
    else:
        return jsonify({'error': 'Name and email are required'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
