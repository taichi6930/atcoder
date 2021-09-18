import collections


def main():
    n = int(input())
    A = [int(input()) for _ in range(n)]
    C = collections.Counter(A)

    if len(C.keys()) == n:
        print('Correct')
        return

    print(C.most_common()[0][0], list(
        set([i + 1 for i in range(n)])-set(C.keys()))[0])


if __name__ == '__main__':
    main()
