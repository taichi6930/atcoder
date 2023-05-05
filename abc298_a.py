n = int(input())
S = list(input())
print("YNeos"[not ((S.count("o") > 0) and (S.count("x") == 0)) :: 2])
