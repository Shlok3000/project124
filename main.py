from flask import Flask, jsonify, request 

app = Flask(__name__)

data = [
     {
        'id': 1,
        'Contact': u'9987644456',
        'name': u'Raju', 
        'done': False
    },
    {
        'id': 2,
        'Contact': u'9876543222',
        'Name': u'Rahul',
        'done': False
    }
]

@app.route('/')
def Welcome():
    return("These are the contacts of Rahul and Raju")

@app.route('/add-data',methods = ["POST"])
def addTask():
    if not request.json:
        return jsonify({
            "status": "error",
            "messages":"Please provide the Data",
        },400)

    contact = {
        'id': data[-1]['id'] + 1,
        'title': request.json["title"],
        'description': request.json.get("description", ""),
        'done': False
    }
    data.append(contact)
    return jsonify({
        'status': 'success',
        'message': 'task added successfully'
    })

@app.route('/get-data')
def getTask():
    return jsonify({
        "data":data
    })

if(__name__ == "__main__"):
    app.run(debug = True)