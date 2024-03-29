import math


def main():
    n, q = map(int,  input().split())
    s = input()
    LRList = [list(map(int,  input().split())) for _ in range(q)]
    sumAC = 0
    ACList = [0] * (n)
    for i in range(1, n):
        if s[i - 1: i + 1] == 'AC':
            sumAC += 1
        ACList[i] = sumAC
    for j in range(q):
        l, r = LRList[j][0], LRList[j][1]
        print(ACList[r-1] - ACList[l-1])


if __name__ == '__main__':
    main()
