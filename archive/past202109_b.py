def int2strWithArray(Array):
    return list(map(lambda x: str(x), Array))


def main():
    n, m = map(int, input().split())
    A = set(list(map(int, input().split())))
    B = set(list(map(int, input().split())))
    C = sorted(list(A & B))
    print(' '.join(int2strWithArray(C)))


if __name__ == '__main__':
    main()
