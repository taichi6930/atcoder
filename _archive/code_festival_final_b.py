def str2intWithArray(Array):
    return list(map(lambda x: int(x), Array))


def main():
    n = str2intWithArray(list(input()))
    n1 = n[0::2]
    n2 = n[1::2]

    print(sum(n1) - sum(n2))


if __name__ == '__main__':
    main()
