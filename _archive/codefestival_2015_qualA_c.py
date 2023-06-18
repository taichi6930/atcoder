
def main():
    n, t = map(int, input().split())
    AB = []
    A = 0
    B = 0

    for i in range(n):
        a, b = map(int, input().split())
        AB.append(a - b)
        A += a
        B += b
    if B > t:
        print(-1)
        return
    if A <= t:
        print(0)
        return

    AB = sorted(AB, reverse=True)

    for j in range(n):
        A -= AB[j]
        if A <= t:
            print(j + 1)
            return


if __name__ == '__main__':
    main()
