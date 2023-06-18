n = int(input())
S = list(input())
T = list(input())
for i in range(n):
    s, t = S[i], T[i]
    if (
        s == t
        or (s in ["l", "1"] and t in ["l", "1"])
        or (s in ["0", "o"] and t in ["0", "o"])
    ):
        continue
    exit(print("No"))
print("Yes")
