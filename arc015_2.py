def main():
    ans = [0] * 6

    n = int(input())
    for _ in range(n):
        a, b = map(float, input().split())

        if a >= 35:
            ans[0] += 1
        elif a >= 30:
            ans[1] += 1
        elif a >= 25:
            ans[2] += 1

        if b >= 25:
            ans[3] += 1
        elif a >= 0 and b < 0:
            ans[4] += 1
        elif a < 0:
            ans[5] += 1

    print(" ".join(list(map(lambda x: str(x), ans))))


if __name__ == '__main__':
    main()
