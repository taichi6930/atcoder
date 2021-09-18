def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = []
    for i in range(n):
        B.append([A[i], i])

    B.sort(reverse=True)

    for j in range(n):
        print(B[j][1] + 1)


if __name__ == '__main__':
    main()
