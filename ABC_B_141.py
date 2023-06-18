s = input()
a = s[0::2]
b = s[1::2]
print("Yes" if a.count("L") == 0 and b.count("R") == 0 else "No")
