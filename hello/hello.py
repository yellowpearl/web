
bind="0.0.0.0:8080"


def query_func(lst):
    query = lst['QUERY_STRING']
    body = [bytes(i + '\n', 'ascii') for i in query.split('&')]
    return body


def wsgi_application(environ, start_response):
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain')
    ]
    body = query_func(environ)
    start_response(status, headers)
    return body
