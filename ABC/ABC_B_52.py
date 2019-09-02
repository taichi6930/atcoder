n = int(input())
s = list(input())
x = 0
maxNum = 0
for i in range(n):
    if s[i] == "I":
        x += 1
    else:
        x -= 1
    if x > maxNum:
        maxNum = x
print(maxNum)
