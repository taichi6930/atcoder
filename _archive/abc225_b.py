def main():
    n = int(input())
    s = [0] * n
    ans = 'No'

    for i in range(n - 1):
        a, b = map(int, input().split())
        s[a - 1] += 1
        s[b - 1] += 1

    for j in range(n):
        if s[j] == n - 1:
            ans = 'Yes'
            break

    print(ans)


if __name__ == '__main__':
    main()
