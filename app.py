import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import flask_pymongo
from bson.objectid import ObjectId

app = Flask(__name__)


app = Flask(__name__)
app.config["MONGO_DBNAME"] = "pcbuilder"
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_task')
def get_tasks():
    return "Hello world ...again"


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
