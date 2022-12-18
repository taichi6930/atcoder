a, b = map(int, input().split())
stab = str(b / a) + '000'
print('{:.03f}'.format(float(stab[:5]) +
      (1 / 1000 if int(stab[5]) >= 5 else 0)))
