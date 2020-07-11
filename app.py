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


@app.route('/all_builds')
def all_builds():
    return render_template("allbuilds.html", builds=mongo.db.build.find())

# Add build form


@app.route('/')
@app.route('/add_build')
def add_build():
    build_names = mongo.db.build.find()
    motherboards = mongo.db.motherboard.find()
    processors = mongo.db.processor.find()
    processorcoolers = mongo.db.processorcooler.find()
    memory = mongo.db.memory.find()
    graphicscards = mongo.db.graphicscard.find()
    harddrives = mongo.db.harddrive.find()
    powersupplies = mongo.db.powersupply.find()
    cases = mongo.db.case.find()
    return render_template('/addbuild.html', motherboards=motherboards, processors=processors, processorcoolers=processorcoolers, memory=memory, graphicscards=graphicscards, harddrives=harddrives, powersupplies=powersupplies, cases=cases, build_names=build_names)


@app.route('/insert_build', methods=['POST'])
def insert_build():
    build = mongo.db.build
    build.insert_one(request.form.to_dict())
    return redirect(url_for('all_builds'))


@app.route('/edit_build/<build_id>')
def edit_build(build_id):
    the_build = mongo.db.build.find_one({"_id": ObjectId(build_id)})
    all_cases = mongo.db.case.find(),
    all_graphics_cards = mongo.db.graphicscard.find(),
    all_hard_drives = mongo.db.harddrive.find(),
    all_memory = mongo.db.memory.find(),
    all_motherboards = mongo.db.motherboard.find(),
    all_power_supplies = mongo.db.powersupply.find(),
    all_processors = mongo.db.processor.find(),
    all_processor_coolers = mongo.db.processorcooler.find()
    return render_template('editbuild.html', build=the_build, cases=all_cases, graphicscards=all_graphics_cards, harddrives=all_hard_drives, memory=all_memory, motherboards=all_motherboards, powersupplies=all_power_supplies, processors=all_processors, processorcoolers=all_processor_coolers ) 


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
