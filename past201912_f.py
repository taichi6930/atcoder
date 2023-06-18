import collections

def main():
    S = list(input())
    a = collections.deque()
    ans = collections.deque()
    swi = True

    for s in S:
        ans.append(s)
        if s.isupper():
            swi = not(swi)
        if swi:
            a.append(''.join(list(ans)).capitalize())
            ans = collections.deque()
    O = sorted(a)
    st = ''
    for o in O:
        st += o[:-1] + o[-1].upper()
    print(st)


if __name__ == '__main__':
    main()
