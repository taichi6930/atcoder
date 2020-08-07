
import collections
import math


def main():
    n, k = map(int, input().split())
    aList = sorted(list(map(int, input().split())), reverse=True)
    bList = aList.copy()
    a = aList[-1]
    bList[-1] = 0
    if n == 1:
        print(math.ceil(math.exp(a/k)))

    for i in range(n - 1):
        bList[i] = math.ceil(math.log2(aList[i] / a))

    print(bList)
    # if sum(bList) < k:
    #     num = math.floor((n - sum(bList)) / n)
    #     print(math.ceil(math.exp(a / num)))
    # # if k == 0:
    #     print(aList)


if __name__ == '__main__':
    main()
