n = list(str(input()))
nr = list(reversed(n))

su = 0

for i in range(len(n)):
    if nr[i] == "0":
        su += 1
        continue
    break

n = list(reversed(nr[su:]))
print("Yes" if n == nr[su:] else "No")
