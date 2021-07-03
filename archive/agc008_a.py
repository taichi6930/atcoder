x, y = map(int, input().split())
cnt = 0
if x > y and x * y > 0:
    cnt += 2
elif x * y < 0 or (x > y and (x == 0 or y == 0)):
    cnt += 1
print(cnt + abs(abs(x)-abs(y)))
