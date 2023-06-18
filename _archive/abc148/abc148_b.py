n = int(input())
s, t = map(str, input().split())
string = ""
for i in range(n):
    string += s[i:i+1] + t[i:i+1]
print(string)
