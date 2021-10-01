def str2intWithArray(Array):
    return list(map(lambda x: int(x), Array))


def main():
    k = int(input())
    A, B = list(map(str, input().split()))
    A, B = str2intWithArray(list(A)[::-1]), str2intWithArray(list(B)[::-1])
    sumA = sum([k ** i * A[i] for i in range(len(A))])
    sumB = sum([k ** i * B[i] for i in range(len(B))])
    print(sumA * sumB)


if __name__ == '__main__':
    main()
