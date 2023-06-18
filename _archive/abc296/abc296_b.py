S = [input() for _ in range(8)]
alphaList = list("abcdefghijklmnopqrstuvwxyz")


for i, s in enumerate(S):
    if '*' not in s:
        continue
    exit(print(f'{alphaList[s.index("*")]}{8 - i}'))
