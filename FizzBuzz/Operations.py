def GenericStatement(mod,ret,num): 
  if num > 0:
    if num % mod == 0:
      return ret
  return ""

def Fizz(num):
  return GenericStatement(3,"Fizz",num)

def Buzz(num):
  return GenericStatement(5,"Buzz",num)

def Bazz(num):
  return GenericStatement(7,"Bazz",num)

def Fozz(num):
  return GenericStatement(13,"Fozz",num)

#What checks are used?
operations = [Fizz,Buzz]