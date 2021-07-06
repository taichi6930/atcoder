def main():
    S = list(input())
    n = len(S)

    wordList = ["dream", "dreamer", "erase", "eraser"]

    for i in range(10 ** 6):
        # 最初に、今の末端の長さを記録していく
        l = n

        # 文字列があるかどうかをチェックする
        for word in wordList:
            if word == "".join(S[max(0, n - len(word)):]):
                l -= len(word)
                break
        # 数値が同じであれば、何も消せてないということなので、終了
        if l == n:
            print("NO")
            return
        # 文字列がないのであれば終了
        if l == 0:
            print("YES")
            return

        S = S[0: l]
        n = l


if __name__ == '__main__':
    main()
