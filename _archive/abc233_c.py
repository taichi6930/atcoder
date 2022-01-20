import collections


def main():
    n, x = map(int, input().split())
    lis = collections.deque([1])
    for i in range(n):
        arr = list(map(int, input().split()))
        l = arr[0]
        A = arr[1:]
        lis2 = collections.deque()
        for a in A:
            for k in lis:
                if k * a > x:
                    continue
                lis2.append(k * a)
        lis = lis2
    print(collections.Counter(list(lis))[x])


if __name__ == '__main__':
    main()
