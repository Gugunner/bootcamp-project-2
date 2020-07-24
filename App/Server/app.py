from flask import Flask, render_template, redirect, jsonify
from flask_cors import CORS
import pymongo
import sys
sys.path.insert(1,"./services")
import create_data
import config

conn = f"mongodb+srv://{config.user}:{config.password}@cluster0.uatil.mongodb.net/Project_2?retryWrites=true&w=majority"
client = pymongo.MongoClient(conn)
db = client.Project_2
collection_computing = db.computing_efficiency
collection_microprocessors = db.microprocessor_clock_speed
collection_price_changes = db.price_changes_in_consumer_goods_and_services_in_the_usa_1997_2017

app = Flask(__name__)
CORS(app)
@app.route('/project-2-api/computing_efficiency.json', methods=['GET'])
def get_computing():
    mongo_values = collection_computing.find()
    return jsonify(create_data.create_computing_efficiency_dict(mongo_values))

@app.route('/project-2-api/microprocessor_clock_speed.json', methods=['GET'])
def get_microprocessors():
    mongo_values = collection_microprocessors.find()
    return jsonify(create_data.create_microprocessor_clock_speed_dict(mongo_values))

@app.route('/project-2-api/price_changes_in_consumer_goods_and_services_in_the_usa_1997_2017.json', methods=['GET'])
def get_price_changes():
    mongo_values = collection_price_changes.find()
    return jsonify(create_data.create_price_changes_in_consumer_goods_and_services_in_the_usa_1997_2017_dict(mongo_values))

if __name__ == '__main__':
    app.run(debug=True)
