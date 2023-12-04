f = open("puzzleinput.txt", "r")

puzzleInputList = f.readlines()

allNumbers = []

# if there's only one number in the line: it's 11, 77, 55 etc
# only the first and last numbers should be appended, work backwards and forwards to check the first occurance

# go through all the items from the puzzle list
for item in puzzleInputList:
  itemDigits = []
  itemReversed = item[::-1] # one list to check from the front, and one to check from the back
  for char in item:
    if char.isnumeric():
      itemDigits.append(char)
      break
  for char in itemReversed:
    if char.isnumeric():
      itemDigits.append(char)
      break
  allNumbers.append(int("".join(itemDigits)))


resultFile = open('result.txt', 'w')
resultFile.write(str(sum(allNumbers)))

resultFile.close()
f.close()