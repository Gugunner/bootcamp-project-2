from flask import Flask, render_template, redirect
import pymongo

import sys
sys.path.insert(1,"./services")
import create_data

conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)
db = client.test_db
collection = db.test_collection

app = Flask(__name__)

@app.route('/')
def index():
    values = collection.find()
    create_data.create_test_json(values)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
