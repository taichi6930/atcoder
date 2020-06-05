import sys
readline = sys.stdin.readline


def main():
    a, b = map(int, readline().rstrip().split())
    print(a * b)


if __name__ == '__main__':
    main()
