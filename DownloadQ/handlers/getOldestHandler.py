import json
from services import fileInteraction

def handleGetOldest(self):

  print(f'Running handleGetOldest()')

  result = [fileInteraction.todoReadFirstLine()]

  self.send_response(200)
  self.send_header('content-type', 'application/json')
  self.end_headers()
  self.wfile.write(json.dumps(result).encode())