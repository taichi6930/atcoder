import collections


def main():
    n, q = map(int, input().split())
    A = list(map(int, input().split()))
    B = {}
    C = {}

    for z in range(n):
        num = A[z]
        if num in B.keys():
            B[num].append(z + 1)
            C[num] += 1
            continue
        B[num] = collections.deque([z + 1])
        C[num] = 1

    for i in range(q):
        x, k = map(int, input().split())
        if x not in B.keys():
            print(-1)
            continue
        if C[x] < k:
            print(-1)
            continue
        print(B[x][k - 1])


if __name__ == '__main__':
    main()
