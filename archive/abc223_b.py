import collections


def main():
    s = collections.deque(list(input()))
    n = len(s)
    ss = collections.deque()

    for i in range(n):
        x = s.popleft()
        s += [x]
        ss.append(''.join(s))
    ss = sorted(ss)
    print(ss[0])
    print(ss[-1])


if __name__ == '__main__':
    main()
