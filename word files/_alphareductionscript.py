file = open("words_alphamodified.txt", encoding = "utf8")
##file = open("oxford_alphamodified.txt", encoding = "utf8")
otherWords = file.read().split("\n")
file.close()

words = []

count = 0

##for word in otherWords:
##    if len(words) == 0:
##           words.append(word)
##    else:
##        found = False
##
##        count = count + 1
##        if count == 10000:
##            print(len(words))
##            print()
##            count = 0
##        
##        for i in range(len(words)):
##            if word < words[i]:
##                temp = words[0:i] + [word] + words[i:len(words)]
##                words = temp
##                found = True
##                break
##
##        if not found:
##            words.append(word)

for word in otherWords:
    if len(word) > 2 and len(word) < 8:
        if word.isalpha():
            words.append(word)

print("done")

wfile = open("words37.txt", mode='w', encoding="utf8")
##wfile = open("oxford_modified.txt", mode='w', encoding="utf8")

for word in words:
    wfile.write(word + '\n')

wfile.close()
