n = int(input())
a = [105, 135, 165, 189, 195]
for i in range(5):
    a[i] = 1 if n >= a[i] else 0
print(sum(a))
