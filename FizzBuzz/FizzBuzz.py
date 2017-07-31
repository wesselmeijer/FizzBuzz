#Used to make a rule regarding multiples of numbers
#just give the multitude and return value and then the input number
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

#Maximum number that will be iterated towards
maxNum = 100

#Can add Bazz or Fozz to this array to include them in compilation
operations = [Fizz,Buzz]

for i in range (1,maxNum+1):
  output = ""
  for item in operations:
    output += item(i)
  if output == "":
    output = str(i)
  print(output)
  