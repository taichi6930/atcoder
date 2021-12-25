def main():
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    n = int(input())
    arr = []
    a = n
    for i in range(100):
        if a % 26 == 0:
            b = a // 26 - 1
            c = 26
        else:
            b = a // 26
            c = a % 26
        a = b
        arr.insert(0, c)

        if b == 0:
            break

    string = ''
    for l in range(len(arr)):
        string += alpha[arr[l] - 1]
    print(string)


if __name__ == '__main__':
    main()
