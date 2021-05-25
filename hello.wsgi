def application(environ, start_response):
  status = '200 OK'
  headers = [('Content-type', 'text/plain; charset=utf-8')]
  body = 'hello, world This is from CICD pipeline. Welcome '.encode('utf-8')
  start_response(status, headers)
  return [body]
