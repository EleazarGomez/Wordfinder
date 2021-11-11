from itertools import permutations
from itertools import combinations

letters = []
userInput = str(input("Enter letters: "))
letters = list(userInput)

file = open("lexicon37.txt", encoding = "utf8")
words = file.read().split("\n")
##lines = file.readlines()
file.close()

##wordsOxford = []
##
##for line in lines:
##    data = line.split(" ")
##    word = data[0].lower()
##    if word != "\n":
##        wordsOxford.append(word)
        
##file = open("words_modified.txt")
##otherWords = file.read().split("\n")
##file.close()

wordsToPrint = []

for L in range(0, len(letters) + 1):
    for subset in combinations(letters, L):
        use = []
        for x in subset:
            use.append(x)
        if (use != []):
            usePerm = permutations(use)
            for y in list(usePerm):
                word = ""
                for z in y:
                    word += z
                if word in words:
                    if word not in wordsToPrint and len(word) > 2:
                        print(word)
                        wordsToPrint.append(word)


colsToPrint = []
count = 0
colCount = 0
wordCount = len(wordsToPrint)
tempCol = []

while count < wordCount:
    if colCount < 25:
        tempCol.append(wordsToPrint[count])
    else:
        colsToPrint.append(tempCol)
        tempCol = []
        colCount = 0
        tempCol.append(wordsToPrint[count])

    count += 1
    colCount += 1

colsToPrint.append(tempCol)
        
numColumns = len(colsToPrint)

##print()
##print("============ Your Words Are ============")
##print()

totalWords = len(wordsToPrint)
bigWords = 0
for i in range(len(wordsToPrint)):
    if len(wordsToPrint[i]) > 3:
        bigWords += 1


print()
print("=========== total: ", totalWords, " || ", "over: ", bigWords, " ===========", sep="")
print()

formatString = "{:<7s}"

for i in range(len(colsToPrint[0])):
    row = ""
    for col in colsToPrint:
        try:
            row += formatString.format(col[i])
        except:
            row += formatString.format("")
    print(row)
