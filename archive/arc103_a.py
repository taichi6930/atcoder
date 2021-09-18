import collections
def main():
    _ = int(input())
    V = list(map(int, input().split()))
    CV0, CV1 = collections.Counter(V[0::2]), collections.Counter(V[1::2])

    V0no1Num, V0no1Cnt, V0no2Cnt = CV0.most_common()[
        0][0], CV0.most_common()[0][1], 0
    if len(CV0.keys()) != 1:
        V0no2Cnt = CV0.most_common()[1][1]
    V1no1Num, V1no1Cnt, V1no2Cnt = CV1.most_common()[
        0][0], CV1.most_common()[0][1], 0
    if len(CV1.keys()) != 1:
        V1no2Cnt = CV1.most_common()[1][1]

    print(len(V) - (min((V0no1Cnt + V1no2Cnt),  (V0no2Cnt + V1no1Cnt))
                    if V0no1Num == V1no1Num else (V0no1Cnt + V1no1Cnt)))


if __name__ == '__main__':
    main()
