def main():
    n, m = map(int,  input().split())
    hList = list(map(int,  input().split()))
    hAns = [1] * n
    for i in range(m):
        a, b = map(int,  input().split())
        if hList[a - 1] > hList[b - 1]:
            hAns[b - 1] = 0
            continue
        if hList[a - 1] < hList[b - 1]:
            hAns[a - 1] = 0
            continue
        hAns[a - 1] = 0
        hAns[b - 1] = 0
    print(sum(hAns))


if __name__ == '__main__':
    main()
