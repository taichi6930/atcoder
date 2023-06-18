def main():
    n = int(input())
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    dx, dy = x2 - x1, y2 - y1
    le = (dx ** 2 + dy ** 2) ** 0.5 / 2
    for i in range(n):
        a, b = map(int, input().split())
        B = - 2 * le * (dy * (a - x1) - dx * (b - y1)) / (dx ** 2 + dy ** 2)
        A = ((a - x1) * 2 * le + dy * B - le * dx) / dx
        print(A, B)


if __name__ == '__main__':
    main()
