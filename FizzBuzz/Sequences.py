import math

def fibb():
  old = 0
  new = 1
  result = [1]
  for i in range (0,30):
    result += [old+new]
    intermediate = old+new
    old = new
    new = intermediate
  return result

def seq(max):
  if type(max) == int:
    return list(range(1,max))
  return []

def wesSequence():
  item = 2
  storage = item
  result = [item]
  for i in range (0,6):
    storage = int(round((item * 4) / 3))
    result += [storage]
    item = storage
  return result