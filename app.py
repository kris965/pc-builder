"""
ObjectId: used to generate Id
Flask: Allow template functionality
Pymongo: Allows interaction between python and MongoDB
"""
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
    """
    Default route to send user to home page
    """
    return render_template("index.html")


@app.route('/all_builds')
def all_builds():

    """
    Renders the allbuild template to see all builds
    """

    return render_template("allbuilds.html", builds=mongo.db.build.find())

# Add build form


@app.route('/add_build')
def add_build():

    """
Finds all data in collection to populate the options in the forms
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
    return render_template(
        '/addbuild.html',
        motherboards=motherboards,
        processors=processors,
        processorcoolers=processor_coolers,
        memory=memory,
        graphicscards=graphics_cards,
        harddrives=hard_drives,
        powersupplies=power_supplies,
        cases=cases,
        build_names=build_names)


@app.route('/insert_build', methods=['POST'])
def insert_build():

    """Takes form options and turns it into a
    dictionary and sends it to the database"""

    build = mongo.db.build
    build.insert_one(request.form.to_dict())
    return redirect(url_for('all_builds'))


@app.route('/edit_build/<build_id>')
def edit_build(build_id):

    """
     Gets the build's Id to populate the forms
     with that build values for editing
     finds all collection data to populate the forms with options
    """

    build = mongo.db.build.find_one({"_id": ObjectId(build_id)})
    motherboards = mongo.db.motherboard.find()
    processors = mongo.db.processor.find()
    processor_coolers = mongo.db.processorcooler.find()
    memory = mongo.db.memory.find()
    graphics_cards = mongo.db.graphicscard.find()
    hard_drives = mongo.db.harddrive.find()
    power_supplies = mongo.db.powersupply.find()
    cases = mongo.db.case.find()
    return render_template(
        'editbuild.html',
        motherboards=motherboards,
        processors=processors,
        processorcoolers=processor_coolers,
        memory=memory,
        graphicscards=graphics_cards,
        harddrives=hard_drives,
        powersupplies=power_supplies,
        cases=cases, build=build)


@app.route('/update_build/<build_id>', methods=["POST"])
def update_build(build_id):

    """
    Gets the build Id and sends updated data to mongo
    Then gets redirected to all builds page
    """
    build = mongo.db.build
    build_params = {
        'build_name': request.form.get('build_name'),
        'motherboard': request.form.get('motherboard'),
        'processor': request.form.get('processor'),
        'processor_cooler': request.form.get('processor_cooler'),
        'memory': request.form.get('memory'),
        'graphics_card': request.form.get('graphics_card'),
        'hard_drive': request.form.get('hard_drive'),
        'power_supply': request.form.get('power_supply'),
        'case': request.form.get('case')
        }

    build.replace_one({'_id': ObjectId(build_id)}, build_params)
    return redirect(url_for('all_builds'))


@app.route('/delete_build/<build_id>')
def delete_build(build_id):

    """
       Gets the build Id and deletes it form the database
       Then gets redirected to all builds page
    """

    mongo.db.build.delete_one({'_id': ObjectId(build_id)})
    return redirect(url_for('all_builds'))


@app.route('/search_motherboard')
def search_motherboard():

    """
       Sends user to search page and populates form option
    """
    motherboards = mongo.db.motherboard.find()
    return render_template(
        '/search-by-motherboard.html',
        motherboards=motherboards)


@app.route('/search_processor')
def search_processor():

    """
       Sends user to search page and populates form option
    """
    processors = mongo.db.processor.find()
    return render_template(
        '/search-by-processor.html',
        processors=processors)


@app.route('/search_processor_cooler')
def search_processor_cooler():

    """
       Sends user to search page and populates form option
    """
    processor_coolers = mongo.db.processorcooler.find()
    return render_template(
        '/search-by-processor-cooler.html',
        processor_coolers=processor_coolers)


@app.route('/search_memory')
def search_memory():

    """
       Sends user to search page and populates form option
    """
    memory = mongo.db.memory.find()
    return render_template('/search-by-memory.html', memory=memory)


@app.route('/search_graphics_card')
def search_graphics_card():

    """
       Sends user to search page and populates form option
    """
    graphics_cards = mongo.db.graphicscard.find()
    return render_template(
        '/search-by-graphics-card.html',
        graphics_cards=graphics_cards)


@app.route('/search_hard_drive')
def search_hard_drive():

    """
       Sends user to search page and populates form option
    """
    hard_drives = mongo.db.harddrive.find()
    return render_template(
        '/search-by-hard-drive.html',
        hard_drives=hard_drives)


@app.route('/search_power_supply')
def search_power_supply():

    """
       Sends user to search page and populates form option
    """
    power_supplies = mongo.db.powersupply.find()
    return render_template(
        '/search-by-power-supply.html',
        powersupplies=power_supplies)


@app.route('/search_case')
def search_case():

    """
       Sends user to search page and populates form option
    """
    cases = mongo.db.case.find()
    return render_template('/search-by-case.html', cases=cases)


@app.route('/search_build_by_motherboard', methods=['POST'])
def search_build_by_motherboard():

    """
       Searches for builds containing selected option
       And redirects to page showing the results
    """

    build = mongo.db.build.find()
    search = request.form.get('search_build_by_motherboard')
    motherboard_search = mongo.db.build.find(
        {"motherboard": {"$regex": search}})
    count = motherboard_search.count()
    return render_template(
        'search-results-motherboard.html',
        motherboard_search=motherboard_search,
        build=build,
        count=count,
        search=True)


@app.route('/search_build_by_processor', methods=['POST'])
def search_build_by_processor():

    """
       Searches for builds containing selected option
       And redirects to page showing the results
    """

    build = mongo.db.build.find()
    search = request.form.get('search_build_by_processor')
    processor_search = mongo.db.build.find({"processor": {"$regex": search}})
    count = processor_search.count()
    return render_template(
        'search-results-processor.html',
        processor_search=processor_search,
        build=build,
        count=count,
        search=True)


@app.route('/search_build_by_processor_cooler', methods=['POST'])
def search_build_by_processor_cooler():

    """
       Searches for builds containing selected option
       And redirects to page showing the results
    """

    build = mongo.db.build.find()
    search = request.form.get('search_build_by_processor_cooler')
    processor_cooler_search = mongo.db.build.find(
        {"processor_cooler": {"$regex": search}})
    count = processor_cooler_search.count()
    return render_template(
        'search-results-processor-cooler.html',
        processor_cooler_search=processor_cooler_search,
        build=build,
        count=count,
        search=True)


@app.route('/search_build_by_memory', methods=['POST'])
def search_build_by_memory():

    """
       Searches for builds containing selected option
       And redirects to page showing the results
    """

    build = mongo.db.build.find()
    search = request.form.get('search_build_by_memory')
    memory_search = mongo.db.build.find({"memory": {"$regex": search}})
    count = memory_search.count()
    return render_template(
        'search-results-memory.html',
        memory_search=memory_search,
        build=build,
        count=count,
        search=True)


@app.route('/search_build_by_graphics_card', methods=['POST'])
def search_build_by_graphics_card():

    """
       Searches for builds containing selected option
       And redirects to page showing the results
    """

    build = mongo.db.build.find()
    search = request.form.get('search_build_by_graphics_card')
    graphics_card_search = mongo.db.build.find(
        {"graphics_card": {"$regex": search}})
    count = graphics_card_search.count()
    return render_template(
        'search-results-graphics-card.html',
        graphics_card_search=graphics_card_search,
        build=build,
        count=count,
        search=True)


@app.route('/search_build_by_hard_drive', methods=['POST'])
def search_build_by_hard_drive():

    """
       Searches for builds containing selected option
       And redirects to page showing the results
    """

    build = mongo.db.build.find()
    search = request.form.get('search_build_by_hard_drive')
    hard_drive_search = mongo.db.build.find({"hard_drive": {"$regex": search}})
    count = hard_drive_search.count()
    return render_template(
        'search-results-hard-drive.html',
        hard_drive_search=hard_drive_search,
        build=build,
        count=count,
        search=True)


@app.route('/search_build_by_power_supply', methods=['POST'])
def search_build_by_power_supply():

    """
       Searches for builds containing selected option
       And redirects to page showing the results
    """

    build = mongo.db.build.find()
    search = request.form.get('search_build_by_power_supply')
    power_supply_search = mongo.db.build.find(
        {"power_supply": {"$regex": search}})
    count = power_supply_search.count()
    return render_template(
        'search-results-power-supply.html',
        power_supply_search=power_supply_search,
        build=build,
        count=count,
        search=True)


@app.route('/search_build_by_case', methods=['POST'])
def search_build_by_case():

    """
       Searches for builds containing selected option
       And redirects to page showing the results
    """

    build = mongo.db.build.find()
    search = request.form.get('search_build_by_case')
    case_search = mongo.db.build.find({"case": {"$regex": search}})
    count = case_search.count()
    return render_template(
        'search-results-case.html',
        case_search=case_search,
        build=build,
        count=count,
        search=True)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=False)
