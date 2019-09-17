n, q = map(int, input().split())
# s = input()
s = "ACGT" * 50000
a = 0
for i in range(99999):
    for j in range(99999):
        if s[i:i+2] == "AC":
            a += 1
        if a % 10000 == 0:
            print(a)
print(a)
