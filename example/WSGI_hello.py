from wsgiref.simple_server import make_server #載入WSGI的功能

def my_app(environ, start_response):
    """a simple wsgi application"""
    status = '200 OK' #設定HTTP狀態碼
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return ["Hello World!”] 
	#顯示文字

httpd = make_server('', 8000, my_app) #建立Server，連進port 8000，執行my_app
print "Serving on port 8000..."
httpd.serve_forever()