def base10to(n, b):
    if n // b:
        return base10to(n // b, b) + str(n % b)
    return str(n % b)


n, k = map(int, input().split())
num = str(n)
for i in range(k):
    q = str(base10to(int(num, 8), 9))
    num = ""
    for i in range(len(q)):
        if q[i] == '8':
            num += '5'
        else:
            num += q[i]
print(num)
