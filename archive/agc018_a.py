import collections
def main():
    n, k = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    for i in range(10 ** 9):
        B = collections.deque([list(A)[0]])
        for j in range(len(A) - 1):
            a = A[j + 1] % A[0]
            if a != 0:
                B.append(a)
        if len(B) == 1:
            C = sorted(list(map(lambda x: (x - k), list(A))))
            for l in range(len(A) - 1):
                if C[l + 1] % B[0] == 0:
                    print("POSSIBLE")
                    return
            print("IMPOSSIBLE")
            return
        if len(B) == len(A):
            if sorted(list(B)) == sorted(list(A)):
                print("IMPOSSIBLE")
                return
        A = B.copy()


if __name__ == '__main__':
    main()
