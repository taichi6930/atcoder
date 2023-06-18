n = int(input())
S = list(input())
if S.count("T") * 2 == n:
    exit(print("T" if S[-1] == "A" else "A"))
print("T" if S.count("T") * 2 > n else "A")
