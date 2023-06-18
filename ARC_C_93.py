def main():
    n = int(input())
    A = [0] + list(map(int,  input().split())) + [0]
    sumA = 0
    for i in range(n+1):
        sumA += abs(A[i+1] - A[i])

    for i in range(n):
        ansA = sumA - abs(A[i+1] - A[i]) - \
            abs(A[i + 2] - A[i + 1]) + abs(A[i + 2] - A[i])
        print(ansA)


if __name__ == '__main__':
    main()
