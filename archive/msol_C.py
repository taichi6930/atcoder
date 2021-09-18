import math


def main():
    n, k = map(int,  input().split())
    A = list(map(int,  input().split()))
    for i in range(n - k):
        print('Yes' if A[k+i] > A[i] else 'No')


if __name__ == '__main__':
    main()
