def main():
    n = int(input())
    A = list(map(int,  input().split()))
    cnt = 0
    for a in range(n):
        if ((a + 1) * A[a]) % 2 == 1:
            cnt += 1
    print(cnt)


if __name__ == '__main__':
    main()
