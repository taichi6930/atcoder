n = int(input())
abcList = list(input())
abcNumList = []
if n != 1:
    for i in range(n-1):
        s = list(input())
        abcList = s * abcList

print(abcList)
