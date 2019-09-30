import fractions
a, b = map(int, input().split())
abMax = fractions.gcd(a, b)
gcdList = [1]
if fractions.gcd(a, b) % 2 == 0:
    gcdList.append(2)
for i in range(1, int((abMax+1)/2)):
    c = 2*i + 1
    if a % c == 0 and b % c == 0:
        swi = 0
        for k in gcdList:
            if fractions.gcd(k, c) != 1:
                swi = 1
                break
        if swi == 0:
            gcdList.append(c)

print(len(gcdList))
