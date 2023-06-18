import collections


def main():
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    AB = A + B
    C = collections.Counter(AB)
    D = []

    for key in sorted(C.keys()):
        if C[key] == 1:
            D.append(str(key))
    print(" ".join(D))


if __name__ == '__main__':
    main()
