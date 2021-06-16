from enum import Enum

class ROUTES(Enum):
  ROOT        = '^/$'
  OVERVIEW    = '^/overview$'
  GET         = '^/get$'
  GET_ALL     = '^/get/all$'
  ADD         = '^/add$'
  DELETE      = '^/delete/[^/]*$'
  DELETE_ALL  = '^/delete/all$'
  FINISH      = '^/finish/[^/]*$'
  FINISH_ALL  = '^/finish/all*$'
  FAVICON     = '^/favicon.ico$'
