def main():
    a, b, k, l = map(int, input().split())

    ans = 0

    # まず、k // lの数だけ、B円でみかんを買う
    ans += (k // l) * b
    k -= (k // l) * l

    # 残りのみかんを買う
    ans = ans + min(b, a * k)

    print(ans)


if __name__ == '__main__':
    main()
