S = input()

for i in range(10 ** 9):
    k = len(S)
    if k == 0:
        exit(print('YES'))
    lis = ['dream', 'erase', 'dreamer', 'eraser']
    swi = False
    for li in lis:
        lenli = len(li)
        t = S[max(0, k - lenli):]
        if t == li:
            S = S[:k - lenli]
            swi = True
            break
    if not(swi):
        exit(print('NO'))
