def main():
    n, m = map(int, input().split())
    A = [list(input()) for _ in range(2 * n)]

    ANS = [[z + 1, 0] for z in range(2 * n)]

    for i in range(1, m + 1):
        for j in range(n):
            player1 = ANS[2 * j][0]
            player2 = ANS[2 * j + 1][0]
            player1hand = A[ANS[2 * j][0] - 1][i - 1]
            player2hand = A[ANS[2 * j + 1][0] - 1][i - 1]

            if player1hand != player2hand:
                if [player1hand, player2hand] in [['G', 'C'], ['C', 'P'], ['P', 'G']]:
                    ANS[2 * j][1] += 1
                else:
                    ANS[2 * j + 1][1] += 1

        ANS = sorted(sorted(ANS), reverse=True, key=lambda x: x[1])

    for q in range(2 * n):
        print(ANS[q][0])


if __name__ == '__main__':
    main()
