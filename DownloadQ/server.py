from http.server import HTTPServer, BaseHTTPRequestHandler
import re
from pathlib import Path
from config import config
from routes import ROUTES
from handlers import rootHandler, getAllHandler, getOldestHandler, notFoundHandler

class ServerHandler(BaseHTTPRequestHandler):
  def do_GET(self):

    print(f'Received GET request ({self.path})')

    if re.search(ROUTES.ROOT.value, self.path):
      rootHandler.handleRoot(self)
    elif re.search(ROUTES.GET_OLDEST.value, self.path):
      getOldestHandler.handleGetOldest(self)
    elif re.search(ROUTES.GET_ALL.value, self.path):
      getAllHandler.handleGetAll(self)
    else:
      notFoundHandler.handle404(self)

def run():
    PORT = 6969
    server = HTTPServer(('', PORT), ServerHandler)
    print(f'Server running on port {PORT}')
    server.serve_forever()

if __name__ == '__main__':
  todo = config.todoFileLocation
  finished = config.finishedFileLocation
  todoPath = Path(todo)
  finishedPath = Path(finished)

  if not todoPath.exists() and not todoPath.is_fifo():
    print(f'Missing file "{todo}", creating it now.')
    open(todo, 'x').close()

  if not finishedPath.exists() and not finishedPath.is_fifo():
    print(f'Missing file "{finished}", creating it now.')
    open(finished, 'x').close()

  run()