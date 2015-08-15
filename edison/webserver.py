from wsgiref.simple_server import make_server

def my_app(environ, start_response):
    """a simple wsgi application"""
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return ["abc"]

port = 8000

httpd = make_server('0.0.0.0', port, my_app)
print "Serving on port " + str(port)
httpd.serve_forever()