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
@app.route('/home_page')
def home_page():
    return render_template("index.html")


@app.route('/all_builds')
def all_builds():
    return render_template("allbuilds.html", builds=mongo.db.build.find())

# Add build form


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
    motherboards = mongo.db.motherboard.find()
    processors = mongo.db.processor.find()
    processorcoolers = mongo.db.processorcooler.find()
    memory = mongo.db.memory.find()
    graphicscards = mongo.db.graphicscard.find()
    harddrives = mongo.db.harddrive.find()
    powersupplies = mongo.db.powersupply.find()
    cases = mongo.db.case.find()
    return render_template('editbuild.html', motherboards=motherboards, processors=processors, processorcoolers=processorcoolers, memory=memory, graphicscards=graphicscards, harddrives=harddrives, powersupplies=powersupplies, cases=cases, build=the_build)


@app.route('/update_build/<build_id>', methods=["POST"])
def update_build(build_id):
    build = mongo.db.build
    build.update({'_id': ObjectId(build_id)},
                 {
        'build_name': request.form.get('build_name'),
        'motherboard': request.form.get('motherboard'),
        'processor': request.form.get('processor'),
        'processor_cooler': request.form.get('processor_cooler'),
        'memory': request.form.get('memory'),
        'graphics_card': request.form.get('graphics_card'),
        'hard_drive': request.form.get('hard_drive'),
        'power_supply': request.form.get('power_supply'),
        'case': request.form.get('case')

    })
    return redirect(url_for('all_builds'))


@app.route('/delete_build/<build_id>')
def delete_build(build_id):
    mongo.db.build.remove({'_id': ObjectId(build_id)})
    return redirect(url_for('all_builds'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
