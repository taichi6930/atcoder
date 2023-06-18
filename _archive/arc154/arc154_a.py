n = int(input())
a = list(input())
b = list(input())
aa = []
bb = []
mod = 998244353

for i in range(n):
    aa.append(str(min(int(a[i]), int(b[i]))))
    bb.append(str(max(int(a[i]), int(b[i]))))
print((int(''.join(aa)) % mod * int(''.join(bb)) % mod) % mod)
