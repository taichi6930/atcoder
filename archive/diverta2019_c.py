def main():
    n = int(input())
    ans = 0
    aNum, baNum, bNum = 0, 0, 0
    for i in range(n):
        s = list(input())
        # 最初がB、最後がAの文字列（BXA）を探す
        if s[0] == "B" and s[-1] == "A":
            baNum += 1
        else:
            # 最初がBの文字列（BX）を探す
            if s[0] == "B":
                bNum += 1
            # 最後がAの文字列（XA）を探す
            if s[-1] == "A":
                aNum += 1

        # 内部のABを探す
        for j in range(len(s) - 1):
            if s[j] == "A" and s[j + 1] == "B":
                ans += 1

    if baNum == 0:
        ans += min(aNum, bNum)
    elif aNum + bNum == 0:
        ans += baNum - 1
    else:
        ans += min(aNum, bNum) + baNum
    print(ans)


if __name__ == '__main__':
    main()
