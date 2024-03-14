from pprint import *


def main():
    n, m = map(int, input().split())
    SC = [None for _ in range(2 ** n)]

    for _ in range(m):
        s, c = map(str, input().split())
        s = list(s)
        sums = 0
        for z in range(n):
            if s[z] == 'Y':
                sums += 2 ** z
        c = int(c)
        if SC[sums] == None:
            SC[sums] = c
        SC[sums] = min(c, SC[sums])

    for i in range(2 ** n - 1):
        if SC[i] is None:
            continue
        for j in range(i + 1, 2 ** n):
            if SC[j] is None:
                continue
            if SC[i | j] is None:
                SC[i | j] = SC[i] + SC[j]
                continue
            SC[i | j] = min(SC[i] + SC[j], SC[i | j])

    print(-1 if SC[-1] is None else SC[-1])
    print(SC)


if __name__ == '__main__':
    main()
