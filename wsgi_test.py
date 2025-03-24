def application(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return [b'Hello from WSGI!']

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    httpd = make_server('', 8888, application)
    print('Serving on port 8888...')
    httpd.serve_forever() 