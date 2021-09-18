import collections


def main():
    s = list(input())
    d = collections.deque(s + ['.'])
    lenS = len(s)
    # 2文字のみ
    if lenS >= 2:
        d.append('..')
        for i in range(lenS - 1):
            s2 = s[i: i + 2]
            d += [s2[0] + s2[1], s2[0] + '.', '.' + s2[1]]

    # 3文字のみ
    if lenS >= 3:
        d.append('...')
        for i in range(lenS - 2):
            s2 = s[i: i + 3]
            d += [
                s2[0] + s2[1] + s2[2],
                s2[0] + s2[1] + '.',
                s2[0] + '.' + s2[2],
                '.' + s2[1] + s2[2],
                '..' + s2[2],
                '.' + s2[1] + '.',
                s2[0] + '..'
            ]

    print(len(set(d)))


if __name__ == '__main__':
    main()
