import collections


def main():
    s = list(input())
    C = collections.deque(['.'])
    if len(s) >= 3:
        C += collections.deque(['...'])
    if len(s) >= 2:
        C += collections.deque(['..'])

    for i in range(len(s)):
        s1 = s[i]
        # 1文字に該当する文字列を出して、Cに入れる
        C += collections.deque(s1)

        if len(s) - i < 2:
            continue

        s12 = ''.join(s[i: i + 2])
        s2 = s[i + 1]
        # 2文字目に該当する文字列を出して、Cに入れる
        C += collections.deque([s12, s1 + '.', '.' + s2])

        if len(s) - i < 3:
            continue
        s13 = ''.join(s[i: i + 3])
        s23 = ''.join(s[i + 1: i + 3])
        s3 = s[i + 2]
        C += collections.deque([s13,
                                s12 + '.',
                                '.' + s23,
                                s1 + '.' + s3,
                                '..' + s3,
                                '.' + s2 + '.',
                                s1 + '..'])
    print(len(set(C)))


if __name__ == '__main__':
    main()
