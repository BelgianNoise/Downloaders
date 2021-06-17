from config import config
import os

def todoReadFirstLine():
  return readFirstLine(f'/{config.todoFileLocation[1:]}')

def finishedRedFirstLine():
  return readFirstLine(f'/{config.finishedFileLocation[1:]}')

def readFirstLine(filename):
  file = open(os.getcwd() + filename, 'r')
  result = file.readline().rstrip()
  file.close()
  return result
