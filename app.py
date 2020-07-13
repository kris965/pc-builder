import os
from os import path
from bson.objectid import ObjectId
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo


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
    """
This is a comment
written in
more than just one line
"""

    build_names = mongo.db.build.find()
    motherboards = mongo.db.motherboard.find()
    processors = mongo.db.processor.find()
    processor_coolers = mongo.db.processorcooler.find()
    memory = mongo.db.memory.find()
    graphics_cards = mongo.db.graphicscard.find()
    hard_drives = mongo.db.harddrive.find()
    power_supplies = mongo.db.powersupply.find()
    cases = mongo.db.case.find()
    return render_template('/addbuild.html', motherboards=motherboards, processors=processors, processorcoolers=processor_coolers, memory=memory, graphicscards=graphics_cards, harddrives=hard_drives, powersupplies=power_supplies, cases=cases, build_names=build_names)


@app.route('/insert_build', methods=['POST'])
def insert_build():
    build = mongo.db.build
    build.insert_one(request.form.to_dict())
    print(request.form.to_dict())
    return redirect(url_for('all_builds'))


@app.route('/edit_build/<build_id>')
def edit_build(build_id):
    update_build = mongo.db.build.find_one({"_id": ObjectId(build_id)})
    motherboards = mongo.db.motherboard.find()
    processors = mongo.db.processor.find()
    processor_coolers = mongo.db.processorcooler.find()
    memory = mongo.db.memory.find()
    graphics_cards = mongo.db.graphicscard.find()
    hard_drives = mongo.db.harddrive.find()
    power_supplies = mongo.db.powersupply.find()
    cases = mongo.db.case.find()
    return render_template('editbuild.html', motherboards=motherboards, processors=processors, processorcoolers=processor_coolers, memory=memory, graphicscards=graphics_cards, harddrives=hard_drives, powersupplies=power_supplies, cases=cases, build=update_build)


@app.route('/update_build/<build_id>', methods=["POST"])
def update_build(build_id):
    build = mongo.db.build
    build_params = {'build_name': request.form.get('build_name'),
                    'motherboard': request.form.get('motherboard'),
                    'processor': request.form.get('processor'),
                    'processor_cooler': request.form.get('processor_cooler'),
                    'memory': request.form.get('memory'),
                    'graphics_card': request.form.get('graphics_card'),
                    'hard_drive': request.form.get('hard_drive'),
                    'power_supply': request.form.get('power_supply'),
                    'case': request.form.get('case')
                    }

    build.update({'_id': ObjectId(build_id)}, build_params)
    return redirect(url_for('all_builds'))


@app.route('/delete_build/<build_id>')
def delete_build(build_id):
    mongo.db.build.remove({'_id': ObjectId(build_id)})
    return redirect(url_for('all_builds'))


@app.route('/search_motherboard')
def search_motherboard():
    build_names = mongo.db.build.find()
    motherboards = mongo.db.motherboard.find()
    processors = mongo.db.processor.find()
    processor_coolers = mongo.db.processorcooler.find()
    memory = mongo.db.memory.find()
    graphics_cards = mongo.db.graphicscard.find()
    hard_drives = mongo.db.harddrive.find()
    power_supplies = mongo.db.powersupply.find()
    cases = mongo.db.case.find()
    return render_template('/search-by-motherboard.html', motherboards=motherboards, processors=processors, processorcoolers=processor_coolers, memory=memory, graphicscards=graphics_cards, harddrives=hard_drives, powersupplies=power_supplies, cases=cases, build_names=build_names)


@app.route('/search_processor')
def search_processor():
    build_names = mongo.db.build.find()
    motherboards = mongo.db.motherboard.find()
    processors = mongo.db.processor.find()
    processor_coolers = mongo.db.processorcooler.find()
    memory = mongo.db.memory.find()
    graphics_cards = mongo.db.graphicscard.find()
    hard_drives = mongo.db.harddrive.find()
    power_supplies = mongo.db.powersupply.find()
    cases = mongo.db.case.find()
    return render_template('/search-by-processor.html', motherboards=motherboards, processors=processors, processorcoolers=processor_coolers, memory=memory, graphicscards=graphics_cards, harddrives=hard_drives, powersupplies=power_supplies, cases=cases, build_names=build_names)


@app.route('/search_processor_cooler')
def search_processor_cooler():
    build_names = mongo.db.build.find()
    motherboards = mongo.db.motherboard.find()
    processors = mongo.db.processor.find()
    processor_coolers = mongo.db.processorcooler.find()
    memory = mongo.db.memory.find()
    graphics_cards = mongo.db.graphicscard.find()
    hard_drives = mongo.db.harddrive.find()
    power_supplies = mongo.db.powersupply.find()
    cases = mongo.db.case.find()
    return render_template('/search-by-processor-cooler.html', motherboards=motherboards, processors=processors, processorcoolers=processor_coolers, memory=memory, graphicscards=graphics_cards, harddrives=hard_drives, powersupplies=power_supplies, cases=cases, build_names=build_names)


@app.route('/search_memory')
def search_memory():
    build_names = mongo.db.build.find()
    motherboards = mongo.db.motherboard.find()
    processors = mongo.db.processor.find()
    processor_coolers = mongo.db.processorcooler.find()
    memory = mongo.db.memory.find()
    graphics_cards = mongo.db.graphicscard.find()
    hard_drives = mongo.db.harddrive.find()
    power_supplies = mongo.db.powersupply.find()
    cases = mongo.db.case.find()
    return render_template('/search-by-memory.html', motherboards=motherboards, processors=processors, processorcoolers=processor_coolers, memory=memory, graphicscards=graphics_cards, harddrives=hard_drives, powersupplies=power_supplies, cases=cases, build_names=build_names)


@app.route('/search_graphics_card')
def search_graphics_card():
    build_names = mongo.db.build.find()
    motherboards = mongo.db.motherboard.find()
    processors = mongo.db.processor.find()
    processor_coolers = mongo.db.processorcooler.find()
    memory = mongo.db.memory.find()
    graphics_cards = mongo.db.graphicscard.find()
    hard_drives = mongo.db.harddrive.find()
    power_supplies = mongo.db.powersupply.find()
    cases = mongo.db.case.find()
    return render_template('/search-by-graphics-card.html', motherboards=motherboards, processors=processors, processorcoolers=processor_coolers, memory=memory, graphicscards=graphics_cards, harddrives=hard_drives, powersupplies=power_supplies, cases=cases, build_names=build_names)


@app.route('/search_hard_drive')
def search_hard_drive():
    build_names = mongo.db.build.find()
    motherboards = mongo.db.motherboard.find()
    processors = mongo.db.processor.find()
    processor_coolers = mongo.db.processorcooler.find()
    memory = mongo.db.memory.find()
    graphics_cards = mongo.db.graphicscard.find()
    hard_drives = mongo.db.harddrive.find()
    power_supplies = mongo.db.powersupply.find()
    cases = mongo.db.case.find()
    return render_template('/search-by-hard-drive.html', motherboards=motherboards, processors=processors, processorcoolers=processor_coolers, memory=memory, graphicscards=graphics_cards, harddrives=hard_drives, powersupplies=power_supplies, cases=cases, build_names=build_names)


@app.route('/search_power_supply')
def search_power_supply():
    build_names = mongo.db.build.find()
    motherboards = mongo.db.motherboard.find()
    processors = mongo.db.processor.find()
    processor_coolers = mongo.db.processorcooler.find()
    memory = mongo.db.memory.find()
    graphics_cards = mongo.db.graphicscard.find()
    hard_drives = mongo.db.harddrive.find()
    power_supplies = mongo.db.powersupply.find()
    cases = mongo.db.case.find()
    return render_template('/search-by-power-supply.html', motherboards=motherboards, processors=processors, processorcoolers=processor_coolers, memory=memory, graphicscards=graphics_cards, harddrives=hard_drives, powersupplies=power_supplies, cases=cases, build_names=build_names)


@app.route('/search_case')
def search_case():
    build_names = mongo.db.build.find()
    motherboards = mongo.db.motherboard.find()
    processors = mongo.db.processor.find()
    processor_coolers = mongo.db.processorcooler.find()
    memory = mongo.db.memory.find()
    graphics_cards = mongo.db.graphicscard.find()
    hard_drives = mongo.db.harddrive.find()
    power_supplies = mongo.db.powersupply.find()
    cases = mongo.db.case.find()
    return render_template('/search-by-case.html', motherboards=motherboards, processors=processors, processorcoolers=processor_coolers, memory=memory, graphicscards=graphics_cards, harddrives=hard_drives, powersupplies=power_supplies, cases=cases, build_names=build_names)


@app.route('/search_build', methods=['POST'])
def search_build():
    build = request.form.get("search_build")
    #  creates an index for each of the collections
    mongo.db.build.create_index([("$**", 'text')])
    mongo.db.motherboard.create_index([("$**", 'text')])
    mongo.db.processor.create_index([("$**", 'text')])
    mongo.db.processorcooler.create_index([("$**", 'text')])
    mongo.db.memory.create_index([("$**", 'text')])
    mongo.db.graphicscard.create_index([("$**", 'text')])
    mongo.db.harddrive.create_index([("$**", 'text')])
    mongo.db.powersupply.create_index([("$**", 'text')])
    mongo.db.case.create_index([("$**", 'text')])
    # search with the selected option that comes through the form
    build_names = mongo.db.build.find({"$text": {"$search": search_build}})
    motherboards = mongo.db.motherboard.find({"$text": {"$search": search_motherboard}})
    processors = mongo.db.processor.find({"$text": {"$search": search_processor}})
    processor_coolers = mongo.db.processorcooler.find({"$text": {"$search": search_processor_cooler}})
    memory = mongo.db.memory.find({"$text": {"$search": search_memory}})
    graphics_cards = mongo.db.graphicscard.find({"$text": {"$search": search_graphics_card}})
    hard_drives = mongo.db.harddrive.find({"$text": {"$search": search_hard_drive}})
    power_supplies = mongo.db.powersupply.find({"$text": {"$search": search_power_supply}})
    cases = mongo.db.case.find({"$text": {"$search": search_case}})
    return render_template('search-results.html', build=build, motherboards=motherboards, processors=processors, processorcoolers=processor_coolers, memory=memory, graphicscards=graphics_cards, harddrives=hard_drives, powersupplies=power_supplies, cases=cases, build_names=build_names, search=True)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
