from http.server import HTTPServer, BaseHTTPRequestHandler
import re
from routes import ROUTES
import handlers

class ServerHandler(BaseHTTPRequestHandler):
  def do_GET(self):

    print(f'Received GET request ({self.path})')

    if re.search(ROUTES.ROOT.value, self.path):
      handlers.handleRoot(self)

def run():
    PORT = 6969
    server = HTTPServer(('', PORT), ServerHandler)
    print(f'Server running on port {PORT}')
    server.serve_forever()

if __name__ == '__main__':
  run()