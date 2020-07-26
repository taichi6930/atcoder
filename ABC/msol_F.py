import math
import sys
import collections
import bisect
readline = sys.stdin.readline


def main():
    n = int(readline().rstrip())
    xyuList = [list(map(str, readline().rstrip().split())) for _ in range(n)]
    for i in range(n - 1):
        xyuI = xyuList[i]
        for j in range(i+1, n):
            xyuJ = xyuList[j]
            if (xyuI[2] == "R" and xyuJ[2] == "L") or (xyuI[2] == "L" and xyuJ[2] == "R"):
                if int(xyuI[1]) == int(xyuJ[1]):
                    print(abs(int(xyuI[0]) - int(xyuJ[0])) * 5)
                    return
                else:
                    continue
            if (xyuI[2] == "U" and xyuJ[2] == "D") or (xyuI[2] == "U" and xyuJ[2] == "D"):
                if int(xyuI[0]) == int(xyuJ[0]):
                    print(abs(int(xyuI[1]) - int(xyuJ[1])) * 5)
                    return
                else:
                    continue
            if (abs(int(xyuI[0]) - int(xyuJ[0])) == abs(int(xyuI[1]) - int(xyuJ[1]))):
                print(abs(int(xyuI[1]) - int(xyuJ[1])) * 10)
                return

    print('SAFE')


if __name__ == '__main__':
    main()
