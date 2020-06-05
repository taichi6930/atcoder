import sys
readline = sys.stdin.readline


def main():
    n = int(readline().rstrip())
    sList = [""] * n
    for i in range(n):
        sList[i] = readline().rstrip()
    print(len(set(sList)))


if __name__ == '__main__':
    main()
