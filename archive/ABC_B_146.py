n = int(input())
s = list(input())
string = ""
engList = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
for i in s:
    string += engList[(engList.index(i) + n) % 26]
print(string)