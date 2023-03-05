n = int(input())
cnt = 0
num = 10 ** 8
for _ in range(10 ** 9):
    if cnt == n:
        print(num - 1)
        break
    str_num = str(num)
    if str_num[0] != str_num[1]:
        num += 10 ** 7
        continue
    if str_num[4] != str_num[5]:
        num += 10 ** 3
        continue
    if str_num[6] != str_num[8]:
        num += 1
        continue
    cnt += 1
    num += 1
