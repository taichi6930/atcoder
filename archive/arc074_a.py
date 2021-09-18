import math


def main():
    h, w = map(int, input().split())

    # h,wのどちらかが3等分できればOK
    if h % 3 == 0 or w % 3 == 0:
        print(0)
        return

    # hを切ってみる
    h1, h2 = math.floor(h / 3), math.ceil(h / 3)


if __name__ == '__main__':
    main()
