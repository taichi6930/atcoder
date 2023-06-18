import collections


def main():
    n = int(input())
    XYList = collections.deque()
    XY = collections.deque()
    cnt = 0
    for q in range(n):
        x, y = map(str, input().split())
        XYList.append([x, y])
        XY.append(x + '_' + y)
    C = collections.Counter(XY)
    for i in range(n - 1):
        for j in range(i + 1, n):
            a, b = XYList[i], XYList[j]
            if a[0] == b[0] or a[1] == b[1]:
                continue
            if C[str(a[0]) + '_' + str(b[1])] + C[str(b[0]) + '_' + str(a[1])] == 2:
                cnt += 1
    print(cnt // 2)


if __name__ == '__main__':
    main()
