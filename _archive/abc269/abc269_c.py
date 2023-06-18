a = list(str(bin(int(input())))[::-1][:-2])
lis = [0]

for i, k in enumerate(a):
    newLis = []
    if k == '1':
        for li in lis:
            newLis.append(li + 2 ** i)
    lis += newLis

for li in lis:
    print(li)
