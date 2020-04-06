import pymongo

def app(environ, start_response):
    client = pymongo.MongoClient('10.88.0.103', 27017)
    db = client['testdb']
    collection = db['testcollection']
    testdoc = {
        "Task": "Do a thing",
        "Requirements": {
            "Tomatoes": 3,
            "Potatoes": 7
        }
    }
    try:
        request_body_size = int(environ.get('CONTENT_LENGTH', 0))
    except (ValueError):
        request_body_size = 0
    print(environ)
    print("BENIS")
    print(environ['wsgi.input'].read(request_body_size))
    collection.insert_one(testdoc)
    data = b"Let's do this\n"
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])
