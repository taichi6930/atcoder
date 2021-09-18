def main():
    k, t = map(int, input().split())
    A = list(map(int, input().split())) + [0]

    for i in range(10 ** 9):
        A.sort(reverse=True)
        if A[1] == 0:
            break
        A[0] -= 1
        A[1] -= 1
    print(max(sum(A) - 1, 0))


if __name__ == '__main__':
    main()
