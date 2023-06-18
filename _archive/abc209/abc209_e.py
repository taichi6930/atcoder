def main():
    n = int(input())
    s = [input() for _ in range(n)]
    top = list(map(lambda x: x[0:3], s))
    tail = list(map(lambda x: x[-3:], s))

    winS = []

    for j in range(n):
        if not tail[j] in top:
            winS.append(s[j])
            continue

    for a in range(n):
        ss = s[a]
        if ss[0:3] == ss[-3:]:
            print("Draw")
        elif not ss[-3:] in top:
            print("Takahashi")
        else:
            print("Aoki")


if __name__ == '__main__':
    main()
