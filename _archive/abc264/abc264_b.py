r, c = map(int, input().split())
print('bwlhaictke'[max(abs(r - 8), abs(c - 8)) % 2::2])
