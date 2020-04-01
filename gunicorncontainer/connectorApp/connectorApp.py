def app(environ, start_response):
    data = b"Let's do this\n"
    start_response("200 OK", [
        ("Content-Type", "test/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])
