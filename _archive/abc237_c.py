def main():
    S = list(input())

    for i in range(len(S)):
        if S[-1] != 'a':
            break
        S.pop()
    T = list(reversed(S))

    for j in range(len(S)):
        if S[j] != T[j]:
            print('No')
            return

    print('Yes')


if __name__ == '__main__':
    main()
