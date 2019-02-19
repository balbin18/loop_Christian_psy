words = (input("Enter your sentence: "))

listd = words.split()

wordlist = ["bobo","hayop", "inutil", "gago",]

hasdetected=False

for word in listd:
    for swear in wordlist:
        if word.find(swear)>-1:
            print("*"*len(swear),end="_")
            hasdetected=True
            break
        else:
            hasdetected=False
    if not hasdetected:
        print(word,end="_")
