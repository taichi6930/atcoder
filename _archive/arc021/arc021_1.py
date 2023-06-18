C = [list(map(int, input().split())) for _ in range(4)]
swi = False
for i in range(4):
    for j in range(4):
        if i + 1 < 4:
            if C[i][j] == C[i + 1][j]:
                swi = True
                break
        if j + 1 < 4:
            if C[i][j] == C[i][j + 1]:
                swi = True
                break
print('CONTINUE' if swi else 'GAMEOVER')
