def main():
    a, b, c = map(int, input().split())
    Z = [0, 1, 5, 6]

    #　そもそも最初の段階でZの範囲内であれば終了
    if a % 10 in Z:
        print(a % 10)
        return

    A = [1]
    B = [1]

    for i in range(b):
        k = (A[i] * a) % 10
        if k in A:
            l = A.index(k)
            lenA = len(A)
            A = A[l:]
            b -= lenA - 1
            print(k, l, A, b)
            break

        A.append(k)

    print(A)


if __name__ == '__main__':
    main()
