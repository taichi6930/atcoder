x = input()
chokuList = ['ch', 'o', 'k', 'u']

for st in chokuList:
    x = x.replace(st, '')

print("YES" if x == "" else "NO")
