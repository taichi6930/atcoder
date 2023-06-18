def main():
    n, m = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = [0] * (n - m) + sorted(list(map(int, input().split())))
    print("YES" if (sorted([A[i] - B[i]
          for i in range(n)])[0] >= 0 and m <= n) else "NO")


if __name__ == '__main__':
    main()
