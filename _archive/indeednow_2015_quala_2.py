def main():
    n = int(input())
    indeednow = ''.join(sorted(list('indeednow')))
    for i in range(n):
        indeedwill = ''.join(sorted(list(input())))
        print('YES' if indeedwill == indeednow else 'NO')


if __name__ == '__main__':
    main()
