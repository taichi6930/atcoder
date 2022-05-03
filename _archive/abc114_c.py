from collections import Counter
n = int(input())
ans = 0


def base10int(value, base):
    if (int(value / base)):
        return base10int(int(value / base), base) + str(value % base)
    return str(value % base)


i = 1

for _ in range(1000000):
    num = base10int(i, 4).replace(
        '3', '7').replace('2', '5').replace('1', '3')
    print(num)
    if int(num) > n:
        break
    lisNum = list(num)
    c = Counter(lisNum)
    if lisNum[-1] == '7':
        i += 2
    else:
        i += 1
    if c['0'] != 0:
        continue
    if c['3'] >= 1 and c['5'] >= 1 and c['7'] >= 1:
        ans += 1


print(ans)
