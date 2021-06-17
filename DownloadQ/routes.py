from enum import Enum

class ROUTES(Enum):
  ROOT        = '^/$'
  GET_OLDEST  = '^/get/oldest$'
  GET_ALL     = '^/get/all$'
  ADD         = '^/add$'
  DELETE_ALL  = '^/delete/all$'
  DELETE      = '^/delete/[^/]*$'
  FINISH_ALL  = '^/finish/all*$'
  FINISH      = '^/finish/[^/]*$'
