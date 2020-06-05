s,t = [input() for _ in range(2)]
print("YNeos"[not(s == t[:-1]) and (len(t) - len(s) == 1)::2])