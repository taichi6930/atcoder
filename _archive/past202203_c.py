s = input()
lenS = len(s)
print(s[:(((lenS - 1) % 3) + 1)] + (list("abcdefghijklmnopqrstuvwxyz")[(lenS - 1) // 3 - 1]
      if (lenS - 1) // 3 - 1 >= 0 else ''))
