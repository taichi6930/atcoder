n = int(input())
s = input()
ss = s.replace("bca", "")
ans = (n % 2 != 0) and (ss == "b" or ss == "ca" or ss == "abc")

print(n//2 if ans else -1)
