
def main():
    n, m, q = map(int, input().split())
    pCnt = [[0 for _ in range(m)] for _ in range(n)]
    cnt = [n for _ in range(m)]
    for i in range(q):
        S = list(map(int, input().split()))
        x = S[1]
        if S[0] == 1:
            A = pCnt[x - 1]
            ans = 0
            j = 0
            for j in range(m):
                ans += A[j] * cnt[j]
            print(ans)

        if S[0] == 2:
            y = S[2]
            pCnt[x - 1][y - 1] = 1
            cnt[y - 1] -= 1


if __name__ == '__main__':
    main()
