from flask import Response, Flask, render_template, json, request, redirect, url_for
from flask_pymongo import PyMongo
from bson import ObjectId
app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'techsitution4'

mongo = PyMongo(app)
# showing all audits in list
#@app.route("/audit/<string:audit_id>", methods=["GET", "POST"])
#def show(audit_id):

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("index.html")

@app.route('/audits', methods=['GET', 'POST'])
def audits():
    if request.method == 'GET':
        audits = mongo.db.form.find()
        return render_template('audits.html', audits=audits)
    elif request.method == 'POST':
        data = request.form
        if data["confidential"] == "yes":

            mongo.db.form.insert({
                "confidential": data["confidential"],
                "operator_name": data["operator_name"],
                "occurrence": data["occurrence"],
                "local": data["local"],
                "flight_date": data["flight_date"],
                "flight_number": data["flight_number"],
                "departure": data["departure"],
                "destination": data["destination"],
                "aircraft_type": data["aircraft_type"],
                "aircraft_registration": data["aircraft_registration"],
                "location_of_occurrence": data["location_of_occurrence"],
                "origin_of_the_goods": data["origin_of_the_goods"],
                "description": data["description"],
                "proper_shipping_name": data["proper_shipping_name"],
                "class_division": data["class_division"],
                "subsidary_risk": data["subsidary_risk"],
                "packing_group": data["packing_group"],
                "category": data["category"],
                "type_of_packaging": data["type_of_packaging"],
                "packaging_specification_marking": data["packaging_specification_marking"],
                "no_of_packages": data["no_of_packages"],
                "quantity": data["quantity"],
                "reference_no": data["reference_no"],
                "reference_ticket": data["reference_ticket"],
                "name_and_adrress": data["name_and_adrress"],
                "other_relevant_information": data["other_relevant_information"],
                "name_and_title": data["name_and_title"]

                })



        else :

            mongo.db.form.insert({
                "confidential": data["confidential"],
                "operator_name": data["operator_name"],
                "occurrence": data["occurrence"],
                "local": data["local"],
                "flight_date": data["flight_date"],
                "flight_number": data["flight_number"],
                "departure": data["departure"],
                "destination": data["destination"],
                "aircraft_type": data["aircraft_type"],
                "aircraft_registration": data["aircraft_registration"],
                "location_of_occurrence": data["location_of_occurrence"],
                "origin_of_the_goods": data["origin_of_the_goods"],
                "description": data["description"],
                "proper_shipping_name": data["proper_shipping_name"],
                "class_division": data["class_division"],
                "subsidary_risk": data["subsidary_risk"],
                "packing_group": data["packing_group"],
                "category": data["category"],
                "type_of_packaging": data["type_of_packaging"],
                "packaging_specification_marking": data["packaging_specification_marking"],
                "no_of_packages": data["no_of_packages"],
                "quantity": data["quantity"],
                "reference_no": data["reference_no"],
                "reference_ticket": data["reference_ticket"],
                "name_and_adrress": data["name_and_adrress"],
                "other_relevant_information": data["other_relevant_information"],
                "name_and_title": data["name_and_title"],
                "telephone_no": data["telephone_no"],
                "company_dept_code": data["company_dept_code"],
                "reporter_ref": data["reporter_ref"],
                "address": data["address"],
                "date_signature": data["date_signature"],
                "description_of_the_occurrence": data["description_of_the_occurrence"]

            })

        return redirect(url_for('audits'))

# @app.route('/audits', methods=['GET', 'POST'])
# def audits():
#     if request.methods == 'GET':
#         audits = mongo.db.form.find()
#         return render_template("audits.html", audits=audits)

@app.route('/audits/<string:audit_id>', methods=['GET', 'POST'])
def show(audit_id):
    if request.method == 'GET':
        # Query to get specific ocations
        audit = mongo.db.form.find_one({"_id": ObjectId(audit_id)})
        return render_template('show.html', audit=audit)

# Editing audit
@app.route('/audits/<string:audit_id>/edit', methods=['GET', 'POST'])
def edit(audit_id):
    if request.method == 'GET':

        audit = mongo.db.form.find_one({"_id": ObjectId(audit_id)})
        return render_template("edit.html", audit=audit)
    elif request.method == 'POST':
        edit_data = request.form

        mongo.db.form.update({"_id": ObjectId(audit_id)}, {"$set":{
            "confidential": edit_data["confidential"],
            "occurrence": edit_data["occurrence"],
            "operator_name": edit_data["operator_name"],
            "local": edit_data["local"],
            "flight_date": edit_data["flight_date"],
            "flight_number": edit_data["flight_number"],
            "departure": edit_data["departure"],
            "destination": edit_data["destination"],
            "aircraft_type": edit_data["aircraft_type"],
            "aircraft_registration": edit_data["aircraft_registration"],
            "location_of_occurrence": edit_data["location_of_occurrence"],
            "origin_of_the_goods": edit_data["origin_of_the_goods"],
            #"description": edit_data["description"],
            #"proper_shipping_name": edit_data["proper_shipping_name"],
            #"class_division": edit_data["class_division"],
            #"subsidary_risk": edit_data["subsidary_risk"],
            #"packing_group": edit_data["packing_group"],
            #"category": edit_data["category"],
            #"type_of_packaging": edit_data["type_of_packaging"],
            #"packaging_specification_marking": edit_data["packaging_specification_marking"],
            #"no_of_packages": edit_data["no_of_packages"],
            #"quantity": edit_data["quantity"],
            #"reference_no": edit_data["reference_no"],
            #"reference_ticket": edit_data["reference_ticket"],
            #"name_and_adrress": edit_data["name_and_adrress"],
            #"other_relevant_information": edit_data["other_relevant_information"],
            #"name_and_title": edit_data["name_and_title"],
            #"telephone_no": edit_data["telephone_no"],
            #"company_dept_code": edit_data["company_dept_code"],
            #"reporter_ref": edit_data["reporter_ref"],
            #"address": edit_data["address"],
            #"date_signature": edit_data["date_signature"],
            #"description_of_the_occurrence": edit_data["description_of_the_occurrence"]
            }
        })
        return redirect(url_for("show", audit_id=audit_id))


@app.route('/audits/delete', methods=['POST'])
def delete():
    if request.method == "POST":
        # Query to delete specific
        audit_id = request.form["audit_id"]
        audit = mongo.db.form.remove({"_id": ObjectId(audit_id)})
        # return redirect(url_for('audits', audit_id=audit_id))
        return Response(response=json.dumps({"success": "OK"}), status=200, mimetype="application/json")


if __name__ == '__main__':
    app.run(port=5007,host='0.0.0.0', debug=True)
