def main():
    n = int(input())
    C = [list(map(int, input().split())) for _ in range(n)]
    B = [C[0][i] - min(C[0]) for i in range(n)]
    A = [C[j][0] - B[0] for j in range(n)]

    for a in range(n):
        for b in range(n):
            if C[a][b] != A[a] + B[b]:
                print("No")
                return

    print("Yes")
    print(" ".join(list(map(lambda x: str(x), A))))
    print(" ".join(list(map(lambda x: str(x), B))))


if __name__ == '__main__':
    main()
