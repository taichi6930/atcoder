from collections import Counter


def main():
    n, k = map(int,  input().split())
    a = list(map(int,  input().split()))
    c = Counter(a)
    print(sum(sorted(c.values(), reverse=True)[k: len(c)]))


if __name__ == '__main__':
    main()
