n = list(input())


def is_left_hand(num):
    return int(num) > 0 and int(num) <= 5


ans = 0
swi = True
beforeNum = 0

for i, num in enumerate(n):
    # 最初は500ms
    if i == 0:
        ans += 500
    # 同じ文字である場合、301ms
    elif beforeNum == num:
        ans += 301
    # 同じ手である場合、301ms
    elif is_left_hand(num) == swi:
        ans += 210
    else:
        ans += 100

    # 記録する
    beforeNum = num
    swi = is_left_hand(num)

print(ans)
