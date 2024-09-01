sentence = "the quick brown fox jumps over the lazy dog the dog barks"

wordlist = sentence.split()

mymap = {}

for x in wordlist:
    if x not in mymap:
        mymap[x] = 1
    else:
        mymap[x] += 1
print(mymap)
