s = input()[::-1]
print(len(s) - s.find('a') if s.find('a') != -1 else -1)
