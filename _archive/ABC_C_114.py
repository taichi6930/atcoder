import collections


def main():
    n = int(input())
    cnt = 0
    for i in range(n):
        t = sorted(list(str(i + 1)))
        c = list(collections.Counter(t).keys())
        cnt += 1 if c == ["3", "5", "7"] else 0
    print(cnt)


if __name__ == '__main__':
    main()
