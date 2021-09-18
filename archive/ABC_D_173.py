def main():
    n = int(input())
    A = sorted(list(map(int,  input().split())))
    a = sorted(A[0:n-1] * 2, reverse=True)
    print(max(A) + sum(a[0:n-2]))


if __name__ == '__main__':
    main()
