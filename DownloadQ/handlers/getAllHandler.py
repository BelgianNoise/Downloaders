import json

def handleGetAll(self):

  print(f'Running handleGetAll()')

  

  self.send_response(200)
  self.send_header('content-type', 'applicaion/json')
  self.end_headers()
  self.wfile.write(json.dumps())