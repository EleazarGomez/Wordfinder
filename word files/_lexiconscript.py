file = open("oxford37.txt", encoding = "utf8")
wordsOxford = file.read().split("\n")
file.close()

file = open("words37.txt", encoding = "utf8")
otherWords = file.read().split("\n")
file.close()

words = []

count = 0

while len(wordsOxford) > 0 or len(otherWords) > 0:    
    if len(wordsOxford) == 0:
        words.extend(otherWords)
        otherWords = []
    elif len(otherWords) == 0:
        words.extend(wordsOxford)
        wordsOxford = []
    else:
        word1 = wordsOxford[0]
        word2 = otherWords[0]

        count = count + 1

        if count == 10000:
            print("oxford: " + str(len(wordsOxford)))
            print(word1)
            print("other: " + str(len(otherWords)))
            print(word2)
            print()
            count = 0
            
        dupe = False

        if word1 in words:
            wordsOxford.pop(0)
            dupe = True
        if word2 in words:
            otherWords.pop(0)
            dupe = True
            
        if not dupe:
            if word1 == word2:
                words.append(word1)
                wordsOxford.pop(0)
                otherWords.pop(0)
            else:
                if word1 < word2:
                    words.append(word1)
                    wordsOxford.pop(0)
                else:
                    words.append(word2)
                    otherWords.pop(0)
                

wfile = open("lexicon37.txt", mode='w', encoding="utf8")

for word in words:
    wfile.write(word + '\n')

wfile.close()
