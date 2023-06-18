def int2strWithArray(Array):
    return list(map(lambda x: str(x), Array))


def main():
    n = 1000
    A = sorted(int2strWithArray([i + 1 for i in range(n)]))
    for a in A:
        print(a)


if __name__ == '__main__':
    main()
