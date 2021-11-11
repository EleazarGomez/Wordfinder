file = open("blacklist.txt", encoding = "utf8")
blacklist = file.read().split("\n")
file.close()

file = open("lexicon37.txt", encoding = "utf8")
lexicon = file.read().split("\n")
file.close()

tempBlacklist = []

for bword in blacklist:
    if bword not in tempBlacklist:
        tempBlacklist.append(bword)

blacklist = tempBlacklist

words = []

for word in lexicon:
    if word not in blacklist:
        words.append(word)

print("done")

wfile = open("lexicon37.txt", mode='w', encoding="utf8")

for word in words:
    wfile.write(word + '\n')

wfile.close()

wfile = open("blacklist.txt", mode='w', encoding="utf8")

for bword in blacklist:
    wfile.write(bword + '\n')

wfile.close()
