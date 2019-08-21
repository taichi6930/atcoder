N = int(input())
SVoteList = []
SVoteNum = []
for i in range(N):
    SVote = input()
    if SVote in SVoteList:
        SVoteNum[SVoteList.index(SVote)] += 1
    else:
        SVoteList.append(SVote)
        SVoteNum.append(1)
print(SVoteList[SVoteNum.index(max(SVoteNum))])
