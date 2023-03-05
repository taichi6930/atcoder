S = [list(map(int, input().split())) for _ in range(4)] * 2
print('YNeos'[(min([- (S[i][0] - S[i + 1][0]) * (S[i + 2][1] - S[i + 1][1]) +
                    (S[i][1] - S[i + 1][1]) * (S[i + 2][0] - S[i + 1][0]) for i in range(4)]) < 0)::2])
