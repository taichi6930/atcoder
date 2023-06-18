import collections


def main():
    n = int(input())
    s = []

    for _ in range(n):
        s.extend(list(input()))

    c = collections.Counter(s)

    if c['R'] > c['B']:
        print('TAKAHASHI')
    elif c['R'] < c['B']:
        print('AOKI')
    else:
        print('DRAW')


if __name__ == '__main__':
    main()
