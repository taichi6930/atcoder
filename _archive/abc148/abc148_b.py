n = int(input())
[s, t] = map(str, input().split())
st = ''
for i in range(n):
    st += s[i]
    st += t[i]

print(st)
