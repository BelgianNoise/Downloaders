
def handleRoot(self):

  print(f'Running handleRoot()')

  self.send_response(200)
  self.send_header('content-type', 'text/html')
  self.end_headers()
  self.wfile.write(f'<h1> Server is up and running </h1>'.encode())