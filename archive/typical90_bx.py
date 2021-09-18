
from bisect import bisect_left


def main():
    n = int(input())
    A = list(map(int, input().split()))
    A = A + A
    B = [0] + [None] * 2 * n

    for i in range(2 * n):
        B[i + 1] = B[i] + A[i]
    targetA = sum(A) // 20
    # 小数であれば解はなし
    if targetA * 20 != sum(A):
        print("No")
        return
    for j in range(n):
        ans = 0
        x = bisect_left(B, B[j] + targetA)
        if B[x] == B[j] + targetA:
            print("Yes")
            return
    print("No")


if __name__ == '__main__':
    main()
