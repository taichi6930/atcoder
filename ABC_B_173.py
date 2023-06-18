from collections import Counter


def main():
    n = int(input())
    s = [input() for _ in range(n)]
    c = Counter(s)
    lis = ['AC', 'WA', 'TLE', 'RE']
    for li in lis:
        print(li+' x ' + str(c[li]))


if __name__ == '__main__':
    main()
