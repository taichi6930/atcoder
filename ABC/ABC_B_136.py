n = input()
if len(n) % 2 == 0:
    print(int((100 ** (len(n)/2) - 1) // 11))
