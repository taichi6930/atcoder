def main():
    t = int(input())

    for _ in range(t):
        countList = [0] * 11
        a, b, c = map(int, input().split())
        countList[2] += a
        countList[3] += b
        countList[4] += c

        # 長さ3を全て2つずつ足して長さ6にし、長さ4を足して長さ10を作成
        countList[6] += countList[3] // 2
        countList[3] = countList[3] % 2
        k = min(countList[6], countList[4])
        countList[10] += k
        countList[6] -= k
        countList[4] -= k

        # 長さ4を全て2つずつ足して長さ8にし、長さ2を足して長さ10を作成
        countList[8] += countList[4] // 2
        countList[4] = countList[4] % 2
        l = min(countList[8], countList[2])
        countList[10] += l
        countList[8] -= l
        countList[2] -= l

        # 長さ6と長さ2を2つ足して長さ10を作成
        m = min(countList[6], countList[2] // 2)
        countList[10] += m
        countList[6] -= m
        countList[2] -= m * 2

        # 長さ4と長さ2を3つ足して長さ10を作成
        n = min(countList[4], countList[2] // 3)
        countList[10] += n
        countList[4] -= n
        countList[2] -= n * 3

        # 長さ2を5つ足して長さ10を作成
        countList[10] += countList[2] // 5
        print(countList[10])


if __name__ == '__main__':
    main()
