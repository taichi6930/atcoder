def main():
    T = int(input())
    for t in range(T):
        l, r = map(int, input().split())
        # Aの範囲を求める
        aMin, aMax = l * 2, r

        # aMinがaMaxを超えていたらアウト
        if aMin > aMax:
            print(0)
            continue
        k = aMax - aMin
        print((k + 1) * (k + 2) // 2)


if __name__ == '__main__':
    main()
