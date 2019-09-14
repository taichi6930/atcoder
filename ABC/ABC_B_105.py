n = int(input())
swi = "No"
for a in range(100):
    b = n - 4*a
    if b % 7 == 0 and b >= 0:
            swi = "Yes"
            break
print(swi)
