n, m = map(int, input().split())
mSum, st = 1, 0

gl = int(input())
mSum *= 2 ** int((gl - st)/2)
st = gl
print(mSum)

for i in range(1, m):
    gl = int(input())
    if gl - st == 1:
        mSum = 0
        break
    mSum *= 2 ** int((gl - st)/2)
    st = gl
    print(mSum)

gl = n
if mSum != 0:
    mSum *= 2 ** int((gl - st)/2)

    print(mSum)

print(mSum % 1000000007)
