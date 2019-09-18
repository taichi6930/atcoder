n = int(input())
a = []
for i in range(n):
    string = int(input())
    if a.count(string) == 0:
        a.append(string)
    else:
        a.remove(string)
print(len(a))
