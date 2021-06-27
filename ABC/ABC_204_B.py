n = int(input())
Alist = list(map(int, input().split()))
suma = 0
for a in Alist:
    suma += max(a - 10, 0)
print(suma)
