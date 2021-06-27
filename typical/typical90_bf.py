n, k = map(int, input().split())
aList = []


def pushA(a):
    intA = a
    strA = sum(list(map(lambda x: int(x), list(str(a)))))
    return (intA + strA) % (10 ** 5)


for i in range(k):
    n = pushA(n)
    if aList.count(n) > 0:
        l = len(aList)
        x = aList.index(n)
        aList = aList[x:]
        ansL = (k - l - 1) % (l - x)
        print(aList[ansL])
        exit()

    aList.append(n)

print(aList[-1])
