import collections


def str2intWithArray(Array):
    return list(map(lambda x: int(x), Array))


def main():
    S = int(input())
    s = str2intWithArray(list(str(S)))
    cs = collections.Counter(s)

    for i in range(min(100, 10 ** (len(str(S - 1)) - 1)), min(1000, 10 ** len(str(S - 1))) + 1):
        if i % 8 != 0 or 0 in str2intWithArray(list(str(i))):
            continue
        K = collections.Counter(str2intWithArray(list(str(i))))

        swi = 1
        for key in K.keys():
            if cs[key] < K[key]:
                swi = 0
                break

        if swi == 1:
            print("Yes")
            return
    print("No")


if __name__ == '__main__':
    main()
