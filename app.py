from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from bson import ObjectId
app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'techsitution4'

mongo = PyMongo(app)
# showing all audits in list
#@app.route("/audit/<string:audit_id>", methods=["GET", "POST"])
#def show(audit_id):

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        audits = mongo.db.form.find()
        return render_template('index.html', audits=audits)
    elif request.method == 'POST':
        data = request.form

        mongo.db.form.insert({
            "confidential": data["confidential"],
            "operator_name": data["operator_name"],
            "occurrence": data["occurrence"],
            "local": data["local"],
            "flight-number": data["flight-number"]
            

        })

        return redirect(url_for('hello_world'))

@app.route('/audit/<string:audit_id>', methods=['GET', 'POST'])
def show(audit_id):
    if request.method == 'GET':
        # Query to get specific audit
        audit = mongo.db.form.find_one({"_id": ObjectId(audit_id)})
        return render_template('show.html', audit=audit)

# Editing audit
@app.route('/edit/audit/<string:audit_id>', methods=['GET', 'POST'])
def edit(audit_id):
    if request.method == 'GET':

        audit = mongo.db.form.find_one({"_id": ObjectId(audit_id)})
        return render_template("edit.html", audit=audit)
    elif request.method == 'POST':
        edit_data = request.form

        mongo.db.form.update({"_id": ObjectId(audit_id)}, {"$set":{
            "confidential": edit_data["confidential"],
            "operator_name": edit_data["operator_name"],
            "local": edit_data["local"]
            }
        })
        return redirect(url_for("show", audit_id=audit_id))

if __name__ == '__main__':
    app.run(port=5006,host='0.0.0.0', debug=True)
