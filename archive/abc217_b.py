def main():
    lis = ['ABC', 'ARC', 'AGC', 'AHC']
    ans = 6
    for i in range(3):
        s = input()
        index = lis.index(s)
        ans -= index
    print(lis[ans])


if __name__ == '__main__':
    main()
