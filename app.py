import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

from os import path

if path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["MONGO_DBNAME"] = "pcbuilder"
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)


@app.route('/')
@app.route('/all_builds')
def all_builds():
    return render_template("allbuilds.html", build=mongo.db.build.find())

# Add build form


@app.route('/add_build')
def add_build():
    build_name = mongo.db.build_name.find()
    motherboard = mongo.db.motherboard.find()
    processor = mongo.db.processor.find()
    processorcooler = mongo.db.processorcooler.find()
    memory = mongo.db.memory.find()
    graphicscard = mongo.db.graphicscard.find()
    harddrive = mongo.db.harddrive.find()
    powersupply = mongo.db.powersupply.find()
    case = mongo.db.case.find()
    return render_template('/addbuild.html', motherboard=motherboard, processor=processor, processorcooler=processorcooler, memory=memory, graphicscard=graphicscard, harddrive=harddrive, powersupply=powersupply, case=case, build_name=build_name)


@app.route('/insert_build', methods=['POST'])
def insert_build():
    build = mongo.db.build
    build.insert_one(request.form.to_dict())
    return redirect(url_for('all_builds'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
