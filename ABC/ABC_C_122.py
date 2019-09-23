n, q = map(int, input().split())
s = input()
sACList = [0] * (n-1)
for i in range(n-1):
    if s[i:i+2] == "AC":
        sACList[i] = 1
print(sACList)
for j in range(q):
    l, r = map(int, input().split())
    print(sum(sACList[l-1:r-1]))
# a = 0
# for i in range(99999):
#     for j in range(99999):
#         if s[i:i+2] == "AC":
#             a += 1
#         if a % 10000 == 0:
#             print(a)
# print(a)
