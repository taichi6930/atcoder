def int2strWithArray(Array):
    return list(map(lambda x: str(x), Array))


def main():
    n = int(input())
    print("".join(int2strWithArray(
        [9 if n % 9 == 0 else n % 9] * ((n - 1) // 9 + 1))))


if __name__ == '__main__':
    main()
