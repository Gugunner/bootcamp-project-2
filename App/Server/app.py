from flask import Flask, render_template, redirect, jsonify
from flask_cors import CORS
import pymongo
import sys
sys.path.insert(1,"./services")
import create_data

conn = "mongodb+srv://Raul:bootcamp1234@cluster0.uatil.mongodb.net/Project_2?retryWrites=true&w=majority"
client = pymongo.MongoClient(conn)
db = client.Project_2
collection = db.computing_efficiency
collection2 = db.microprocessor_clock_speed

app = Flask(__name__)
CORS(app)
@app.route('/project-2-api/computing_efficiency.json', methods=['GET'])
def index():
    values = collection.find()
    return jsonify(create_data.create_test_json(values))

@app.route('/project-2-api/microprocessor_clock_speed.json', methods=['GET'])
def index2():
    values = collection2.find()
    print(values)
    return jsonify(create_data.create_microprocessor_clock_speed_dict(values))

if __name__ == '__main__':
    app.run(debug=True)
