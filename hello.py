
def query_func(list):
    body = ''
    query = list['QUERY_STRING']
    i = 0
    while i <= query.count('&')+1:
        body += query[:query.index('&')] + '\n'
        query = query[query.index('&') + 1:]
        i +=1
    body += query[:]
    return body

dictionaty = {
    "QUERY_STRING" : "a=3&c=2&b=1&g=4"
}
query_func(dictionaty)


def wsgi_application(environ, start_response):
    body = ''
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain')
    ]
    start_response(status, headers)
    return body
