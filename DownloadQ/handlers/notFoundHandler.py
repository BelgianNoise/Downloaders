import json

def handle404(self):

  print(f'Running handle404()')

  self.send_response(404)
  self.send_header('content-type', 'text/html')
  self.end_headers()
  self.wfile.write(f'<h1>Page not Found</h1>'.encode())