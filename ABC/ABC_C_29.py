def Base_10_to_n(X, n):
    if (int(X/n)):
        return Base_10_to_n(int(X/n), n)+str(X % n)
    return str(X % n)


alphaList = ["a", "b", "c"]
n = int(input())
for i in range(3**n):
    num = str(Base_10_to_n(i, 3))
    numStr = ""
    print(num)
    # for j in range(len(str(num))):
    #     numStr += alphaList[num[j]]
    # print(numStr)
