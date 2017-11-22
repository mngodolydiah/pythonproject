from flask import Flask, jsonify, request
app = Flask(__name__)

events = [{'name':'hitup'}, {'name':'concert'}]
newname = [{'name': 'amina'}]

@app.route("/api/events" ,  methods=['GET'])
def get_events():
    return jsonify({'events': events})

@app.route("/api/auth/register" ,  methods=['POST'])
def get_name():
    newname1 = {'name': request.get_json(force=True).get('name')}
    newname.append(newname1)
    return jsonify({'newname': newname})

@app.route("/api/auth/login" ,  methods=['POST'])
def get_name():
    newname1 = {'name': request.get_json(force=True).get('name')}
    newname.append(newname1)
    return jsonify({'newname': newname})

@app.route("api/auth/reset-password" ,  methods=['POST'])
def get_name():
    newname1 = {'name': request.get_json(force=True).get('name')}
    newname.append(newname1)
    return jsonify({'newname': newname})

@app.route("/api/events" ,  methods=['POST'])
def get_name():
    newname1 = {'name': request.get_json(force=True).get('name')}
    newname.append(newname1)
    return jsonify({'newname': newname})

@app.route("/api/auth/logout" ,  methods=['POST'])
def get_name():
    newname1 = {'name': request.get_json(force=True).get('name')}
    newname.append(newname1)
    return jsonify({'newname': newname})

@app.route("/api/events/<string:name>" ,  methods=['PUT'])
def get_update(name):
    editevents = [event for event in events if event['name'] == name]
    editevents[0]['name'] = request.json['name']
    return jsonify({'event': editevents[0]})

@app.route("/api/events/<string:name>" ,  methods=['DELETE'])
def get_del(name):
    deleteevents = [event for event in events if event['name'] == name]
    events.remove(deleteevents[0])
    return jsonify({'events': events})


if __name__ == '__main__':
    app.run(debug=True)
