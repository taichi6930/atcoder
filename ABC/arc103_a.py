import collections
import math

alphaList = list("abcdefghijklmnopqrstuvwxyz")


def is_prime(n):
    if n == 1:
        return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True


def main():
    n = int(input())
    V = list(map(int, input().split()))
    V0, V1 = V[0::2], V[1::2]
    CV0, CV1 = collections.Counter(V0), collections.Counter(V1)
    V0no1, V0no2 = CV0.most_common()[0], 0
    if len(CV0.keys()) != 1:
        V0no2 = CV0.most_common()[1]
    V1no1, V1no2 = CV1.most_common()[0], 0
    if len(CV1.keys()) != 1:
        V1no2 = CV1.most_common()[1]

    # V0,V1ともに1種類の時
    if V0no2 == 0 and V1no2 == 0:
        if V0no1[0] == V1no1[0]:
            print(V0no1[1])
            return
        print(0)
        return

    # V0,V1どちらかが1種類の時
    if V0no2 == 0:
        if V0no1[0] == V1no1[0]:
            print(len(V0) * 2 - V0no1[1] - V1no2[1])
            return
        print(len(V0) * 2 - V0no1[1] - V1no1[1])
        return


if __name__ == '__main__':
    main()
