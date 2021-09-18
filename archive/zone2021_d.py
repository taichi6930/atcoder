from collections import deque


def main():
    S = list(input())
    n = len(S)
    T = deque()
    swi = 1

    for s in S:
        if s == "R":
            swi *= -1
            continue

        if swi == 1:
            T.append(s)
            continue

        if swi == -1:
            T.appendleft(s)
            continue

    if swi == -1:
        T.reverse()
    T = list(T)

    cnt = 0
    for i in range(10 ** 8):
        if cnt + 1 >= len(T):
            break
        if T[cnt] != T[cnt + 1]:
            cnt += 1
            continue

        T.pop(cnt + 1)
        T.pop(cnt)

        if cnt == 0:
            cnt += 2
            continue
        cnt -= 1

    print("".join(T))


if __name__ == '__main__':
    main()
