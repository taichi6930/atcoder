

def choose(A, i):
    atcoder = ["a", "t", "c", "o", "d", "e", "r"]
    senser = "NG"
    for ac in atcoder:
        if A[i] == ac:
            senser = "OK"
            return
    print("You will lose")
    return


def main():
    S = list(input())
    T = list(input())
    for i in range(len(S)):
        if not S[i] == T[i]:
            # Sの方が@の場合
            if(S[i] == "@"):
                choose(T, i)
            # Tの方が@の場合
            elif(T[i] == "@"):
                choose(S, i)
            else:
                print("You will lose")
                return

    print("You can win")


if __name__ == '__main__':
    main()
