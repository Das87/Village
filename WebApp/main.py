from flask import Flask, jsonify, render_template, request
import pymongo

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('homepage.html')


# .....main page containing people,village,map,festival
@app.route('/all/')
def all():
    return render_template('dash.html')


# ..add family

@app.route('/all/village/')
def village():
    return render_template('village.html')


@app.route('/all/register/')
def register():
    return render_template('addFamily.html')


# ...People's biodata
@app.route('/all/people/')
def people():
    return render_template('people.html')


@app.route('/all/people/add/')
def add():
    return render_template('addFamily.html')


@app.route('/all/people/info/')
def info():
    return render_template('info.html')


# ....Festival section
@app.route('/all/festival/')
def festival():
    return render_template('festival.html')


# Connect to MongoDB
mongo_uri = "mongodb://localhost:27017"
client = pymongo.MongoClient(mongo_uri)
db = client["family_tree"]
collection = db["people"]


# Route to create a new individual in the family tree
@app.route('/api/people/', methods=['POST'])
def create_person():
    data = request.get_json()
    if "name" in data:
        person = db.people.find_one({"name": data["name"]}, {"_id": 0})
        if person:
            return jsonify({"message": "Person with this name already exists"}), 409
    else:
        return jsonify({"message": "Name is required"}), 400
    result = db.people.insert_one(data)
    return jsonify({"message": "Person added successfully", "id": str(result.inserted_id)}), 201


# ------------------------------------------------------------------------------------------------------------------------
def process_family_member_input(member_type, count_key):
    member_data = []

    count_str = request.form.get(count_key)
    if count_str and count_str.isdigit():
        count = int(count_str)
    else:
        count = 0

    for i in range(1, count + 1):
        member_data.append(request.form.get(f"{member_type}_{i}"))

    return member_data
# --------------------------------------------------------------------------------------------------------------------------------
# POSTING THE DATA IN FAMILY DETAILS
# create family for individual
@app.route('/all/people/add/addFamily/submit/', methods=['POST','GET'])
def family_form():
    if request.method == 'POST':
        name = request.form.get("name")
        father = request.form.get("father")
        mother = request.form.get("mother")
        husband = request.form.get("husband")
        wife = request.form.get("wife")

        son_data = process_family_member_input("Son", "son_count")
        daughter_data = process_family_member_input("Daughter", "daughter_count")
        grandson_data = process_family_member_input("Grandson", "grandson_count")
        granddaughter_data = process_family_member_input("Granddaughter", "granddaughter_count")
        


        brother_data = process_family_member_input("Brother", "brother_count")
        sister_data = process_family_member_input("Sister", "sister_count")

        uncle_data = process_family_member_input("Uncle", "uncle_count")
        aunt_data = process_family_member_input("Aunt", "aunt_count")

        nephew_data = process_family_member_input("Nephew", "nephew_count")
        niece_data = process_family_member_input("Niece", "niece_count")

        cousin_data = process_family_member_input("Cousin", "cousin_count")

        father_in_law_data = process_family_member_input("Father_in_law", "father_in_law_count")
        mother_in_law_data = process_family_member_input("Mother_in_law", "mother_in_law_count")

        brother_in_law_data = process_family_member_input("Brother_in_law", "brother_in_law_count")
        sister_in_law_data = process_family_member_input("Sister_in_law", "sister_in_law_count")

        son_in_law_data = process_family_member_input("Son_in_law", "son_in_law_count")
        daughter_in_law_data = process_family_member_input("Daughter_in_law", "daughter_in_law_count")

        stepfather_data = process_family_member_input("Stepfather", "stepfather_count")
        stepmother_data = process_family_member_input("Stepmother", "stepmother_count")

        stepson_data = process_family_member_input("Stepson", "stepson_count")
        stepdaughter_data = process_family_member_input("Stepdaughter", "stepdaughter_count")

        stepbrother_data = process_family_member_input("Stepbrother", "stepbrother_count")
        stepsister_data = process_family_member_input("Stepsister", "stepsister_count")

        half_brother_data = process_family_member_input("Half_brother", "half_brother_count")
        half_sister_data = process_family_member_input("Half_sister", "half_sister_count")

        godfather_data = process_family_member_input("Godfather", "godfather_count")
        godmother_data = process_family_member_input("Godmother", "godmother_count")

        godchild_data = process_family_member_input("Godchild", "godchild_count")
        bhabhi_data = process_family_member_input("Bhabhi", "bhabhi_count")

        great_grandfather_data = process_family_member_input("Great_grandfather", "great_grandfather_count")
        great_grandmother_data = process_family_member_input("Great_grandmother", "great_grandmother_count")
        
        
        grandfather_data = process_family_member_input("Grandfather", "grandfather_count")
        grandmother_data = process_family_member_input("Grandmother", "grandmother_count")

        great_grandson_data = process_family_member_input("Great_grandson", "great_grandson_count")
        great_granddaughter_data = process_family_member_input("Great_granddaughter", "great_granddaughter_count")

        adoptive_parent_data = process_family_member_input("Adoptive_parent", "adoptive_parent_count")
        adopted_child_data = process_family_member_input("Adopted_child", "adopted_child_count")
        foster_parent_data = process_family_member_input("Foster_parent", "foster_parent_count")

        data_to_insert = {
            "name": name,
            "father": father,
            "mother": mother,
            "son": son_data,
            "daughter": daughter_data,
            "grandson": grandson_data,
            "granddaughter": granddaughter_data,
            "husband": husband,
            "wife": wife,
            "brother": brother_data,
            "sister": sister_data,
            "uncle": uncle_data,
            "aunt": aunt_data,
            "nephew": nephew_data,
            "niece": niece_data,
            "cousin": cousin_data,
            "father_in_law": father_in_law_data,
            "mother_in_law": mother_in_law_data,
            "brother_in_law": brother_in_law_data,
            "sister_in_law": sister_in_law_data,
            "son_in_law": son_in_law_data,
            "daughter_in_law": daughter_in_law_data,
            "stepfather": stepfather_data,
            "stepmother": stepmother_data,
            "stepson": stepson_data,
            "stepdaughter": stepdaughter_data,
            "stepbrother": stepbrother_data,
            "stepsister": stepsister_data,
            "half_brother": half_brother_data,
            "half_sister": half_sister_data,
            "godfather": godfather_data,
            "godmother": godmother_data,
            "godchild": godchild_data,
            "bhabhi": bhabhi_data,
            "great_grandfather": great_grandfather_data,
            "great_grandmother": great_grandmother_data,
            "grandmother":grandmother_data,
            "grandfather":grandfather_data,
            "great_grandson": great_grandson_data,
            "great_granddaughter": great_granddaughter_data,
            "adoptive_parent": adoptive_parent_data,
            "adopted_child": adopted_child_data,
            "foster_parent": foster_parent_data,
        }

        # Insert data into the MongoDB collection
        collection.insert_one(data_to_insert)

    return "Data inserted successfully!"
# -----------------------------------------------------------------------------------------------------------------------------------------


# Route to get all individuals in the family tree
@app.route('/api/people', methods=['GET'])
def get_all_people():
    peoples = list(db.people.find({}, {"_id": 0}))
    return jsonify(peoples)


# Route to get an individual by name
@app.route('/api/people/<name>', methods=['GET'])
def get_person_by_name(name):
    person = db.people.find_one({"name": name}, {"_id": 0})
    if person:
        return jsonify(person)
    return jsonify({"message": "Person not found"}), 404


# Route to update an individual by name
@app.route('/api/people/<name>', methods=['PUT'])
def update_person(name):
    data = request.get_json()
    if "name" in data:
        person = db.people.find_one({"name": name}, {"_id": 0})
        if not person:
            return jsonify({"message": "Person not found"}), 404
    else:
        return jsonify({"message": "Name is required"}), 400

    result = db.people.update_one({"name": name}, {"$set": data})
    if result.modified_count > 0:
        return jsonify({"message": "Person updated successfully"}), 200
    return jsonify({"message": "Person not found"}), 404


# Route to delete an individual by name
@app.route('/api/people/<name>', methods=['DELETE'])
def delete_person(name):
    result = db.people.delete_one({"name": name})
    if result.deleted_count > 0:
        return jsonify({"message": "Person deleted successfully"}), 200
    return jsonify({"message": "Person not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
