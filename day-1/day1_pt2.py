f = open("puzzleinput.txt", "r")

puzzleInputList = f.readlines()

numbersInWords = {
  "one": 1,
  "two": 2,
  "three": 3,
  "four": 4,
  "five": 5,
  "six": 6,
  "seven": 7,
  "eight": 8,
  "nine": 9
}

def getWordNumber(number):
  return numbersInWords.get(number)


def findNumberFromWords(string):
  numberWords = list(numbersInWords.keys())
  result = []
  currentWord = ''
  for char in string:
    if char.isnumeric():
      result.append((char))
    currentWord += char
    for numberWord in numberWords:
      if currentWord.endswith(numberWord):
        result.append(str(getWordNumber(currentWord[-len(numberWord):])))

  return result

allNumbers = []

for item in puzzleInputList:
  numbersInItem = findNumberFromWords(item)
  calibrationValue = "".join([(numbersInItem[0]), (numbersInItem[-1])])
  allNumbers.append(int(calibrationValue))



resultFile = open('resultPartTwo.txt', 'w')
resultFile.write(str(sum(allNumbers)))

resultFile.close()
f.close()