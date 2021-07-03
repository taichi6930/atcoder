s = input()
print(min(s[0::2].count("1") + s[1::2].count("0"),
          s[0::2].count("0") + s[1::2].count("1")))
