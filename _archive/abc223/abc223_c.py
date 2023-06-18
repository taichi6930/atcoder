import collections


def main():
    n = int(input())
    x = 0
    A = collections.deque([])
    B = collections.deque([])
    for _ in range(n):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
        x += a / b
    sumx = sum(x) / 2   # 秒数
    cnt = 0
    d = 0

    for i in range(n):
        if cnt + A[i] / B[i] > sumx:
            print(B[i] * (sumx - cnt) + d)
            return
        cnt += A[i] / B[i]
        d += A[i]


if __name__ == '__main__':
    main()
