import collections


def main():
    # n, p = map(int, input().split())
    # a = list(map(int, input().split()))
    # a = list(map(lambda x: x % 2, a))
    # c = collections.Counter(a)
    # print(c)
    cnt = 1
    for i in range(1, 21):
        cnt *= i
    print(cnt)


if __name__ == '__main__':
    main()
