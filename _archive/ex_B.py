def main():
    n = list(input()[::-1])
    gu = n[1::2]
    ki = n[0::2]
    for g in range(len(gu)):
        gu[g] = int(gu[g])
    for k in range(len(ki)):
        ki[k] = int(ki[k])

    print(sum(gu), sum(ki))


if __name__ == '__main__':
    main()
