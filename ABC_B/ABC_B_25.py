n, a, b = map(int, input().split())
sum = 0
for i in range(n):
    s, d = map(str, input().split())
    sign = (-1 if s == "West" else 1)
    if b <= int(d):
        d = str(b)
    elif a >= int(d):
        d = str(a)
    sum += int(d) * sign

if sum == 0:
    print(0)
elif sum > 0:
    print("East", sum)
else:
    print("West", -1 * sum)
