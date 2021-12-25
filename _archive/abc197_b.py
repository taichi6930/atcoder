def main():
    h, w, x, y = map(int, input().split())
    x, y = x - 1, y - 1
    hwList = []
    for _ in range(h):
        hwList.append(list(input()))

    hListMin, hListMax, wListMin, wListMax = -1, w, -1, h
    for i in range(w):
        if hwList[x][i] == "#":
            if i < y:
                hListMin = i
            if i > y:
                hListMax = min(i, hListMax)

    for j in range(h):
        if hwList[j][y] == "#":
            if j < x:
                wListMin = j
            if j > x:
                wListMax = min(j, wListMax)

    print(hListMax - hListMin - 3 + wListMax - wListMin)


if __name__ == '__main__':
    main()
