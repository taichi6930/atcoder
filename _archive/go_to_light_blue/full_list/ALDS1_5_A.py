def is_nth_bit_set(num: int, n: int):
    # bit演算子の計算
    if num & (1 << n):
        return True
    return False


def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = set()

    for i in range(2 ** n):
        k = 0
        for j in range(n):
            if is_nth_bit_set(i, j):
                k += A[j]
        B.add(k)

    q = int(input())
    M = list(map(int, input().split()))

    for m in M:
        print('yes' if m in B else 'no')


if __name__ == '__main__':
    main()
