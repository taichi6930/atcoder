from decimal import *
n = Decimal(input())
print(n)
print(n-int(((n * 8 + 9).sqrt()-3)/2))
