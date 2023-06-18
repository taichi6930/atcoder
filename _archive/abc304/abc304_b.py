n = input()
print(n[0 : min(3, len(n))] + "0" * max(0, len(n) - 3))
