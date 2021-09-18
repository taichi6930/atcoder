def str2intWithArray(Array):
    return list(map(lambda x: int(x), Array))


def main():
    A = int(input())
    listA = str2intWithArray(list(reversed(str(A))))
    ans = 0
    c = 0
    for i in range(len(listA)):
        c = 1 if c == 0 else c * A
        ans += c * listA[i]
    print(ans)


if __name__ == '__main__':
    main()
