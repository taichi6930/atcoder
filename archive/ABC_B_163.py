import math


def main():
    n, m = map(int,  input().split())
    a = list(map(int,  input().split()))
    print(n - sum(a) if n - sum(a) >= 0 else -1)


if __name__ == '__main__':
    main()
