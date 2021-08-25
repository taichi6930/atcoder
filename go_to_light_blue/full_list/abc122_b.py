def main():
    ACGT = ['A', 'C', 'G', 'T']
    S = list(input())
    ans = 0
    k = 0

    for s in S:
        if s in ACGT:
            k += 1
            continue
        ans = max(ans, k)
        k = 0
    print(max(ans, k))


if __name__ == '__main__':
    main()
