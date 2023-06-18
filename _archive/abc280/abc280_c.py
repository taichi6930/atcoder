S = input()
T = input()

for i in range(len(S)):
    if S[i] == T[i]:
        continue
    exit(print(i + 1))
print(len(T))
