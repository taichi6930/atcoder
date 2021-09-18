def main():
    n, m = map(int, input().split())
    S = [['.' for _ in range(m + 2)]] + \
        [['.'] + list(input()) + ['.'] for _ in range(n)] + \
        [['.' for _ in range(m + 2)]]

    for i in range(1, n + 1):
        string = ''
        for j in range(1, m + 1):
            arr = []
            for k in range(3):
                arr += S[i + k - 1][j - 1: j + 2]
            string += str(arr.count('#'))
        print(string)


if __name__ == '__main__':
    main()
