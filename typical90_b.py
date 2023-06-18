def is_nth_bit_set(num: int, n: int):
    if num & (1 << n):
        return True
    return False


n = int(input())
ans = []

for i in range(2 ** n):
    a = ""
    for j in range(n):
        if is_nth_bit_set(i, j):
            a += "("
            continue
        a += ")"

    b = "" + a

    for j in range(10):
        c = "" + b
        c = c.replace("()", "")
        if c == "":
            ans.append(a)
            break
        if b != c:
            b = c
            continue
        break
ans.sort()

for i in range(len(ans)):
    print(ans[i])
