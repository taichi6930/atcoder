def main():
    s = list(input())
    n = len(s)

    ans = 10 ** 3

    c = set(s)
    for key in c:
        maxKey = 0
        newS = [key] + s + [key]
        numKey = 0
        for i in newS:
            if i == key:
                maxKey = max(numKey, maxKey)
                numKey = 0
                continue
            numKey += 1
        ans = min(maxKey, ans)
    print(ans)


if __name__ == '__main__':
    main()
