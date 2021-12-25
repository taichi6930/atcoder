import collections


def main():
    n = int(input())
    A = []
    B = []
    AB = []
    for i in range(n):
        s = input()
        if list(s)[0] == "!":
            A.append(s[1::])
            AB.append(s[1::])
            continue
        B.append(s)
        AB.append(s)
    C = collections.Counter(AB)
    if len(C.keys()) == len(set(A)) + len(set(B)):
        print("satisfiable")
        return
    print(collections.Counter((list(collections.Counter(A).keys()) +
                               list(collections.Counter(B).keys()))).most_common()[0][0])


if __name__ == '__main__':
    main()
