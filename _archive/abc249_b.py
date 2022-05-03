S = list(input())
swi = [0, 0, 0]

if len(S) != len(set(S)):
    print("No")
    exit()


for i, s in enumerate(S):
    if s.islower():
        swi[0] = 1
    if s.isupper():
        swi[1] = 1

print("Yes" if sum(swi) == 2 else "No")
