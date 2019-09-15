n = int(input())
a = []
for i in range(n):
    string = input()
    if a.count(string) == 0:
        a.append(string)
    else:
        a.remove(string)
print(len(a))
b = list(set(a))
aSum = 0
for i in b:
    if a.count(i) % 2 == 1:
        aSum += 1
print(aSum)
