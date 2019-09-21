n = int(input())
abList = list(map(int, input().split()))
a = abList[0::2]
b = abList[1::2]
print(a, b)
