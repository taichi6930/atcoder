def main():
    n = int(input())
    if n == 1:
        print("Yes")
        return
    h = list(map(int,  input().split()))
    for i in range(n - 1):
        right = h[n - i - 1]
        left = h[n - i - 2]
        if left == right + 1:
            h[n - i - 2] -= 1
        if left > right + 1:
            print('No')
            return

    print('Yes')


if __name__ == '__main__':
    main()
