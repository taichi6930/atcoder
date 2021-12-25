def main():
    s, t = map(int, input().split())
    ans = 0
    for a in range(0, 101):
        ss = a
        if ss > s:
            continue
        for b in range(a, 101):
            ss = a + b
            if ss > s:
                continue
            for c in range(b, 101):
                ss = a + b + c
                tt = a * b * c
                if ss > s or tt > t:
                    continue
                if a == c:
                    ans += 1
                    continue
                if a == b or b == c:
                    ans += 3
                    continue
                ans += 6

    print(ans)


if __name__ == '__main__':
    main()
