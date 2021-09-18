import collections


def main():
    n = int(input())
    A = collections.deque(list(map(int, input().split())))
    B = collections.deque(list(map(int, input().split())))
    AB = collections.deque(sorted([[A[i], B[i]] for i in range(n)]))


if __name__ == '__main__':
    main()
