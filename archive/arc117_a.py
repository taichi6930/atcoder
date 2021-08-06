def int2strWithArray(Array):
    return list(map(lambda x: str(x), Array))


def main():
    a, b = map(int, input().split())
    A = [i + 1 for i in range(a)]
    B = [-(i + 1) for i in range(b)]

    if a > b:
        B[-1] = -(sum(A) + sum(B[0:-1]))
    if a < b:
        A[-1] = -(sum(B) + sum(A[0:-1]))

    print(" ".join(int2strWithArray(A + B)))
    return


if __name__ == '__main__':
    main()
