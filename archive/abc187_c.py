import collections
import math


def is_prime(n):
    if n == 1:
        return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True


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
