import collections


def main():
    n = int(input())
    AB = sorted([list(map(int, input().split())) for _ in range(n)])
    AnsList = [0 for _ in range(n)]
    cnt = 0
    lis = collections.deque()

    for i in range(1, n + 1):
        for j in range(n):
            if cnt >= n:
                break
            if AB[cnt][0] != i:
                break
            lis.append(AB[cnt][1])
            cnt += 1
        lis = collections.deque(sorted(lis, reverse=True))
        if len(lis) <= 0:
            AnsList[i] = AnsList[max(0, i - 1)]
            continue
        AnsList[i - 1] = AnsList[max(0, i - 2)] + lis[0]
        lis.popleft()

    for k in range(n):
        print(AnsList[k])


if __name__ == '__main__':
    main()
