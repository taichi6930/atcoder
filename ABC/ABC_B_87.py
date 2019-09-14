# a, b, c, x = [int(input()) for _ in range(4)]
# cnt = 0
# for i in range(min(a, int(x/500)) + 1):
#     for j in range(min(b, int((x - 500 * i)/100)) + 1):
#         k = (x - 500 * i - 100 * j)
#         if k % 50 == 0 and 0 <= k / 50 <= c:
#             cnt += 1
# print(cnt)

a, b, c, x = [int(input()) for _ in range(4)]
cnt = 0
for i in range(a):
    for j in range(b):
        for k in range(c):
            if a * 500 + b * 100 + c * 50 == x:
                cnt += 1
print(cnt)
