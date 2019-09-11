n = int(input())
w = [input() for i in range(n)]
swi = "Yes"
for i in range(n - 1):
    if w.count(w[i]) > 1 or w[i][-1] != w[i + 1][0]:
        swi = "No"
print(swi)
