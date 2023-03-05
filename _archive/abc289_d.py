n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))
x = int(input())

setY = set()
K = set([0])

for i in range(10 ** 9):
    old_K = K.copy()
    K = set()
    if len(old_K) == 0:
        break
    for k in list(old_K):
        for a in A:
            new_st = k + a
            if new_st == x:
                exit(print('Yes'))
            if new_st > x:
                continue
            if new_st in setY:
                continue
            if new_st in B:
                continue
            setY.add(new_st)
            K.add(new_st)

print('No')
