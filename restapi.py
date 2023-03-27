# from https://pythonbasics.org/flask-rest-api/  

import json
from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route('/Voters', methods=['POST'])
def register_voter():
    record = json.loads(request.data)
    with open('.\Voters.txt', 'r') as f:
        data = f.read()
    if not data:
        records = [record]
    else:
        records = json.loads(data)
        records.append(record)
    with open('.\Voters.txt', 'w') as f:
        f.write(json.dumps(records, indent=2))
    return jsonify(record), 201

@app.route("/Voters/<string:student_id>/", methods=['PUT'])
def voter_update(student_id):
    record = json.loads(request.data)
    new_records = []
    with open('.\Voters.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
        for r in records:
            if r['studentId'] == student_id:
                r['Name'] = record['Name']
                r['Email'] = record['Email']
                r['Year']  = record['Year']
                r['Major'] = record['Major']
            new_records.append(r)
    with open('.\Voters.txt', 'w') as f:
        f.write(json.dumps(new_records, indent=2))
    return jsonify(record)
    
@app.route("/Voters/<string:student_id>/", methods=['DELETE'])
def delete_voter(student_id):
    new_records = []
    record = None
    with open('./Voters.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
        for r in records:
            if r['studentId'] == student_id:
                record = r
                continue
            new_records.append(r)
    with open('.\Voters.txt', 'w') as f:
        f.write(json.dumps(new_records, indent=2))
    return jsonify(record)

@app.route("/Voters/<string:student_id>/", methods=['GET'])
def retrieve_voter(student_id):
    with open('./Voters.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
        for record in records:
            if record['studentId'] == student_id:
                return jsonify(record)
        return jsonify({'error': 'data not found'}), 404


@app.route('/Election', methods=['POST'])
def new_election():
    record = json.loads(request.data)
    with open('.\Elections.txt', 'r') as f:
        data = f.read()
    if not data:
        records = [record]
    else:
        records = json.loads(data)
        records.append(record)
    with open('.\Elections.txt', 'w') as f:
        f.write(json.dumps(records, indent=2))
    return jsonify(record), 201


@app.route("/Election/<int:election_id>/", methods=['GET'])
def retrieve_election(election_id):
    with open('.\Elections.txt','r') as f:
        data = f.read()
        records = json.loads(data)
        for record in records:
            if record['Id'] == election_id:
                return jsonify(record)
        return jsonify({'error': 'data not found'}), 404


@app.route("/Election/<int:election_id>/", methods=['DELETE'])
def delete_election(election_id):
    new_records = []
    record = None
    with open('.\Elections.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
        for r in records:
            if r['Id'] == election_id:
                record = r
                continue
            new_records.append(r)
    with open('.\Elections.txt', 'w') as f:
        f.write(json.dumps(new_records, indent=2))
    return jsonify(record)




@app.route("/Election/<int:election_id>/", methods=['PUT'])
def election_voting(election_id):
    record = json.loads(request.data)
    new_records = []
    with open('.\Elections.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
        for r in records:
            if r['Id'] == election_id:
                r['Name'] = record['Name']
                r['Position'] = record['Position']
                r['Candidate']  = record['Candidate']
                r['count_of_votes'] = count_of_votes=+1
            new_records.append(r)
    with open('.\Elections.txt', 'w') as f:
        f.write(json.dumps(new_records, indent=2))
    return jsonify(record)


app.run(debug=True)
