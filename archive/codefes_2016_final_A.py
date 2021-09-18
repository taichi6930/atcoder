
def main():
    aList = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    text = ""
    H, W = map(int, input().split())
    for h in range(H):
        wList = list(map(str, input().split()))
        if wList.count("snuke") == 1:
            text = aList[wList.index("snuke")] + str(h + 1)
    print(text)


if __name__ == '__main__':
    main()
