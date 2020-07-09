@app.route('/')
@app.route('/get_build')
def get_build():
    return render_template("index.html", build=mongo.db.build.find())