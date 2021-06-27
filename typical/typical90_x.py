
def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if (k - sum(a) - sum(b)) % 2 != 0:
        print("No")
        return

    cnt = 0

    for i in range(n):
        cnt += abs(a[i] - b[i])

    print("Yes" if cnt <= k else "No")


if __name__ == '__main__':
    main()
