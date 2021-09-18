def str2intWithArray(Array):
    return list(map(lambda x: int(x), Array))


def main():
    A, B = map(str, input().split())
    [a100, a10, a1] = str2intWithArray(list(A))
    [b100, b10, b1] = str2intWithArray(list(B))

    ans = max(
        (9 - b100) * 100 + (a10 - b10) * 10 + (a1 - b1),
        (a100 - 1) * 100 + (a10 - b10) * 10 + (a1 - b1),
        (a100 - b100) * 100 + (9 - b10) * 10 + (a1 - b1),
        (a100 - b100) * 100 + (a10 - 0) * 10 + (a1 - b1),
        (a100 - b100) * 100 + (a10 - b10) * 10 + (9 - b1),
        (a100 - b100) * 100 + (a10 - b10) * 10 + (a1 - 0))
    print(ans)


if __name__ == '__main__':
    main()
