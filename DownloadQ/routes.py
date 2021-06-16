from enum import Enum

class ROUTES(Enum):
  ROOT        = '^/$'
  OVERVIEW    = '^/overview$'
  GET         = '^/get$'
  GET_ALL     = '^/get/all$'
  ADD         = '^/add$'
  DELETE      = '^/delete/[^/]*$'
  FAVICON     = '^/favicon.ico$'
