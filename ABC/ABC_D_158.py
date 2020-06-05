s = input()
q = int(input())
flg = 1

for i in range(q):
    query = list(input().split())
    if int(query[0]) == 1:
        flg *= -1
    else:
        f, c = int(query[1]), query[2]
        if f == 1:
            if flg == 1:
                s = c + s
            else:
                s += c
        else:
            flg *= -1
            if flg == 1:
                s += c
            else:
                s = c + s

print(s if flg == 1 else s[::-1])
