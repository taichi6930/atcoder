s, t = [list(input()) for _ in range(2)]
a = []
s = "".join(sorted(s))
t = "".join(sorted(t, reverse=True))
a.append(s)
a.append(t)
print("Yes" if a == sorted(a) and s != t else "No")
