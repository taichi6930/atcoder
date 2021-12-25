import math
n = int(input())
s = input()
top = math.floor(n/2)
swi = 0

for k in range(n):
    if top - k - 1 < 0 or swi > 0:
        break
    else:
        for i in range(top + k * 2):
            t = (top-k)+i
            if s[t:n].count(s[i:t]) > 0:
                swi = top - k
                break

print(swi)

# for i in range(top):
#     print(s[i:top+i], s[top+i:n])

# print("----")

# for i in range(top + 1 * 2):
#     print(s[i:(top-1)+i], s[(top-1)+i:n])

# print("----")

# for i in range(top + 2 * 2):
#     print(s[i:(top-2)+i], s[(top-2)+i:n])

# print("----")

# for i in range(top + 3 * 2):
#     print(s[i:(top-3)+i], s[(top-3)+i:n])

# print("----")

# for i in range(top + 4 * 2):
#     print(s[i:(top-4)+i], s[(top-4)+i:n])

# print("----")

# for i in range(top + 5 * 2):
#     print(s[i:(top-5)+i], s[(top-5)+i:n])


# # 次は2文字
# for i in range(n-1):
#     print(s[i:i + 1], s[i + 1:n])
