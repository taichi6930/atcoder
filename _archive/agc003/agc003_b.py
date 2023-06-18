def main():
    n = int(input())
    A = [int(input()) for _ in range(n)] + [0]
    ans = 0
    for i in range(n):
        # まず、自身の数字の2倍分を引く
        x = A[i] // 2
        ans += x
        A[i] -= x * 2

        # 次に、右隣の数字と同じ数だけ引く
        y = min(A[i], A[i + 1])
        ans += y
        A[i] -= y  # これ必要ないけど一応
        A[i + 1] -= y
    print(ans)


if __name__ == '__main__':
    main()
