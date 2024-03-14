n = int(input())
S = [input() for _ in range(n)]

for i in range(n - 1):
    for j in range(i + 1, n):
        if S[i] + S[j] == "".join(list(reversed(S[i] + S[j]))):
            exit(print("Yes"))
        if S[j] + S[i] == "".join(list(reversed(S[j] + S[i]))):
            exit(print("Yes"))
print("No")
