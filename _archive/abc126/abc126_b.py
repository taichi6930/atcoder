s = input()
a = int(s[:2])
b = int(s[2:])

if a == 0:
    if b == 0:
        print('NA')
        exit()
    if 1 <= b <= 12:
        print('YYMM')
        exit()
    if b > 12:
        print('NA')
        exit()

if 1 <= a <= 12:
    if b == 0:
        print('MMYY')
        exit()
    if 1 <= b <= 12:
        print('AMBIGUOUS')
        exit()
    if 12 < b:
        print('MMYY')
        exit()

if 12 < a:
    if b == 0:
        print('NA')
        exit()
    if 1 <= b <= 12:
        print('YYMM')
        exit()
    if 12 < b:
        print('NA')
        exit()
