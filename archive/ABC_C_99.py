n = int(input())
num = [1, 6, 36, 216, ][::-1]
cnt = 0
i = 0
while 0 < n:
    if n > num[i]:
        cnt += 1
        n -= num[i]
        print("cnt:", cnt, num[i])
    else:
        i += 1
        print("i:", i)

print(cnt)
