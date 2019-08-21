S = input()

sList = []
sSentence = ""

sList.append(S[0])

for i in range(1, len(S)):
    sSentence += S[i]
    if sList[len(sList)-1] != sSentence:
        sList.append(sSentence)
        sSentence = ""
print(len(sList))
