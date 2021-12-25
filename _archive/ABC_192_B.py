s = input()
print("Yes" if s[0::2].islower() and (
    s[1::2].isupper() or s[1::2] == "") else "No")
