# bit演算子の計算
def is_nth_bit_set(num: int, n: int):
    if num & (1 << n):
        return True
    return False


s = input()
sumS = 0


for i in range(0, 2 ** (len(s) - 1)):
    a = [0]
    for j in range(len(s) - 1):
        if is_nth_bit_set(i, j):
            a.append(j + 1)
    a.append(len(s))
    for i in range(len(a) - 1):
        sumS += int(s[a[i]: a[i + 1]])
print(sumS)
