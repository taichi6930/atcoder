w = int(input())


lis = []

for i in [1, 100, 10000]:
    for j in range(1, 100):
        lis.append(str(i * j))

print(len(lis))
print(' '.join(lis))
