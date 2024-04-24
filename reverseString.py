inputUse1 = input("enter a string ")

def reverseString(userIn):
  newString = ""
  dalen = len(userIn)
  for i in range(dalen):
    newString += userIn[dalen - 1 - i]
  return newString


print(reverseString(inputUse1))