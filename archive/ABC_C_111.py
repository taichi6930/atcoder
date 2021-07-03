import collections


def main():
    n = int(input())
    v = list(map(int, input().split()))
    a = v[0::2]
    b = v[1::2]
    ac = collections.Counter(a)
    bc = collections.Counter(b)

    print((len(a) - ac.most_common()[0][1]) +
          (len(b) - bc.most_common()[0][1]))


if __name__ == '__main__':
    main()
