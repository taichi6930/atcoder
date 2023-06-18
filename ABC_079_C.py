s = input()

for i in range(2 ** (len(s) - 1)):
    k = list(s)
    for j in range(len(s) - 1):
        if i >> j & 1:
            k[j] = k[j] + "+"
        else:
            k[j] = k[j] + "-"
    kStr = "".join(k)
    if eval(kStr) == 7:
        print(kStr + "=7")
        break
