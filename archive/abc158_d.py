import math


def main():
    s = list(input())
    q = int(input())
    top = []
    tail = []

    swi = 1
    for i in range(q):
        query = list(map(str, input().split()))
        if len(query) == 1:
            swi *= -1
            continue
        f, c = int(query[1]), query[2]
        if (swi == 1 and f == 1) or (swi == -1 and f == 2):
            top.append(c)
            continue
        tail.append(c)

    string = "".join(top[::-1] + s + tail)
    print(string if swi == 1 else string[::-1])


if __name__ == '__main__':
    main()
