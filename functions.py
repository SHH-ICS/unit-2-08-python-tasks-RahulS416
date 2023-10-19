# TASK: Update both functions to reverse the letters in the name and provide the square root of the users age.

# Returns a string that is the contents of the myName variable written backwards
# ie: passing Atkinson as the parameter would return nosniktA
import math
def reverseName(myName):
  # Write your code here
  result = ''
  for i in range(len(myName)):
    result += myName[-1 * (i+1)]
  return result

# Returns a float value that is the contents of the myAge variable square rooted
# ie: passing 16 as the parameter would return 4.0
def rootAge(myAge):
  # Wrie your code here
  result = math.sqrt(int(myAge))
  return result
