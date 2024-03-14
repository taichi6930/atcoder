n = int(input())
a = [0, 1, 1, 1]

for i in range(n):
    new_a = sum(a[-3:]) % 1000000007
    if new_a == 0:
        exit(print(i))

    a.append(new_a)
    print(i, a[-3:])
