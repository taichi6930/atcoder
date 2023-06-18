s = input()
lenS = len(s)

if s != s[::-1] or s[:lenS // 2] != s[:lenS // 2][::-1] or s[::-1][:lenS // 2] != s[::-1][:lenS // 2][::-1]:
    exit(print('No'))

print('Yes')
