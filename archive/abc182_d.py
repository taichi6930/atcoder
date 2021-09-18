def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = []

    ans = 0
    bMax = 0
    bfin = 0

    for i in range(n):
        B.append(A[i])
        # 移動した最大値を決める
        bMax = max(bMax, bfin + A[i])
        # Bの最後の場所が決まる
        bfin = A[i] + bfin
        # bfinをansに移動させて


if __name__ == '__main__':
    main()
