def inputNum():
    numList = []
    for i in range(5):
        numList.append(int(input()))
    return numList


def kJudge(k):
    for i in range(0, 4):
        for j in range(i, 5):
            if abs(numList[i] - numList[j]) > k:
                return ":("
    return "Yay!"


numList = inputNum()
k = int(input())
print(kJudge(k))
