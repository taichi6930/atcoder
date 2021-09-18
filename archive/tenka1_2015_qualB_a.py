import math
from itertools import accumulate


def main():
    A = [100, 100, 200] + [0] * 17
    for i in range(3, 20):
        A[i] = A[i - 1] + A[i - 2] + A[i - 3]
    print(A[19])


if __name__ == '__main__':
    main()
