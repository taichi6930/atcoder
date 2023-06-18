n = int(input())
a = list(map(int, input().split()))
b = a[0::2][::-1]
c = a[1::2]

b.extend(c)
if n % 2 == 0:
    b = b[::-1]
print(*b)
