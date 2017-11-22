from flask import Flask, jsonify, request
app = Flask(__name__)

events = [{'name':'hitup'}, {'name':'concert'}]
newname = [{'name': 'amina'}]

@app.route("/api/events" ,  methods=['GET'])
def get_events():
    return jsonify({'events': events})

if __name__ == '__main__':
    app.run(debug=True)
