import pymongo

def app(environ, start_response):
    client = pymongo.MongoClient('10.88.0.103', 27017)
    db = client['testdb']
    collection = db['testcollection']
    try:
        request_body_size = int(environ.get('CONTENT_LENGTH', 0))
    except (ValueError):
        request_body_size = 0
    print(environ)
    if environ['REQUEST_METHOD'] == 'POST':
        testdoc = environ['wsgi.input'].read(request_body_size)
        collection.insert_one(testdoc)
        data = { "LOL": "Benis" }
    elif environ['REQUEST_METHOD'] == 'GET':
        #testdoc = environ['wsgi.input'].read(request_body_size)
        data = collection.find()
    else:
        data = { "Status": "Borked" }
    start_response("200 OK", [
        ("Content-Type", "application/json")
    ])
    return iter([data])
