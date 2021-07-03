import sys
readline = sys.stdin.readline


def main():
    n = readline().rstrip()
    k = int(n[-1])
    if k in{2, 4, 5, 7, 9}:
        print("hon")
        return
    if k in{0, 1, 6, 8}:
        print("pon")
        return
    print("bon")


if __name__ == '__main__':
    main()
