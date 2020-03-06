n = int(input())
s = list(input())
q = int(input())

for _ in range(q):
    a1, a2, a3 = input().split()

    # a1 = 1の時
    if a1 == "1":
        s[int(a2) - 1] = a3

    # a1 = 2の時
    else:
        print(len(set(s[int(a2) - 1:int(a3)])))
