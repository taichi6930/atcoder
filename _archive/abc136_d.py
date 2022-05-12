S = list(input())
n = len(S)
T = [1] * n
print(T)


def int2strWithArray(Array):
    return list(map(lambda x: str(x), Array))


for _ in range(10 ** 6):
    swi = True
    for i in range(n):
        if S[i] == 'R':
            if S[i + 1] == 'L':
                continue
            if S[i + 1] == 'R':
                if T[i] != 0:
                    swi = False
                T[i + 2] += T[i]
                T[i] = 0
                continue

        if S[i] == 'L':
            if S[i - 1] == 'R':
                continue
            if S[i - 1] == 'L':
                if T[i] != 0:
                    swi = False
                T[i - 2] += T[i]
                T[i] = 0
                continue

        if S[(n - 1) - i] == 'L':
            if S[(n - 1) - (i + 1)] == 'R':
                continue
            if S[(n - 1) - (i + 1)] == 'L':
                if T[(n - 1) - i] != 0:
                    swi = False
                T[(n - 1) - (i + 2)] += T[(n - 1) - i]
                T[(n - 1) - i] = 0
                continue

        # if S[(n - 1) - i] == 'R':
        #     if S[(n - 1) - (i - 1)] == 'L':
        #         continue
        #     if S[(n - 1) - (i - 1)] == 'R':
        #         if T[(n - 1) - i] != 0:
        #             swi = False
        #         T[(n - 1) - (i - 2)] += T[(n - 1) - i]
        #         T[(n - 1) - i] = 0
        #         continue
    print(T)

    if swi:
        break
print(' '.join(int2strWithArray(T)))
