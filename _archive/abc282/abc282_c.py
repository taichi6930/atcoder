n = int(input())
S = list(input())
swi = False

for i, s in enumerate(S):
    if s == '"':
        swi = not(swi)
        continue
    S[i] = s.replace('.', ',') if swi else s.replace(',', '.')

print(''.join(S))
