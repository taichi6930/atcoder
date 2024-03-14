def main():
    S = input()
    for i in range(3):
        if S[i: i + 3] == 'o' * 3:
            print('o')
            return
        if S[i: i + 3] == 'x' * 3:
            print('x')
            return
    print('draw')


if __name__ == '__main__':
    main()
