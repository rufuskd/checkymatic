import pymongo
import json
from bson.json_util import dumps
from bson.objectid import ObjectId

def app(environ, start_response):
    client = pymongo.MongoClient('mongo.local', 27017)
    db = client['testdb']
    collection = db['testcollection']
    try:
        request_body_size = int(environ.get('CONTENT_LENGTH', 0))
    except (ValueError):
        request_body_size = 0
    if environ['REQUEST_METHOD'] == 'POST':
        testdoc = environ['wsgi.input'].read(request_body_size)
        print(testdoc)
        jsonToPush = json.loads((testdoc.decode('utf8')))
        print(json.dumps(jsonToPush))
        collection.insert_one(jsonToPush)
        data = { "LOL": "Benis" }
        print("POST")
    elif environ['REQUEST_METHOD'] == 'GET':
        data = dumps(collection.find())
        print(data)
        print("GET")
        start_response("200 OK", [
            ("Content-Type", "application/json")
        ])
        return [data.encode('utf-8')]
    elif environ['REQUEST_METHOD'] == 'DELETE':
        print(environ['QUERY_STRING'].split('=')[1])
        collection.delete_one({"_id":ObjectId(environ['QUERY_STRING'].split('=')[1])})
        print("DELETE")
        data = { "LOL": "Benis" }
    else:
        data = { "Status": "Borked" }
    start_response("200 OK", [
        ("Content-Type", "application/json")
    ])
    return [data]
