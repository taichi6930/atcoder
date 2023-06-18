def main():
    k = int(input())
    A = [2]
    B = [1]

    for i in range(k - 1):
        a = A[-1]
        b = B[-1]
        B.append(a)
        A.append(a + b)
    print(A[-1], B[-1])


if __name__ == '__main__':
    main()
