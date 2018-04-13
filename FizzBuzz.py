import Sequences, Operations

#Used to make a rule regarding multiples of numbers
#just give the multitude and return value and then the input number

#Maximum number that will be iterated towards
maxNum = 100

numberSequence = Sequences.wesSequence()

if type(numberSequence) == list and len(numberSequence) != 0: 
  for i in numberSequence:
    if type(i) == int:
      output = str(i) + " - "
      for item in Operations.operations:
        output += item(i)
      if output == str(i) + " - ":
        output = str(i)
      print(output)
  