S = input()
a, b, c = S[0], S[1:-1], S[-1]
if not(a.isupper()) or not(b.isdigit()) or not(c.isupper()) or len(b) != 6:
    exit(print('No'))
print('Yes' if 100000 <= int(b) <= 999999 else 'No')
