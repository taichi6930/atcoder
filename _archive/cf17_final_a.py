
def main():
    s1 = input().split('KIH')
    if len(s1) != 2 or not(s1[0] in ['', 'A']):
        print('NO')
        return
    s2 = s1[1].split('B')
    if len(s2) != 2 or not(s2[0] in ['', 'A']):
        print('NO')
        return
    s3 = s2[1].split('R')
    if len(s3) != 2 or not(s3[0] in ['', 'A']) or not(s3[1] in ['', 'A']):
        print('NO')
        return
    print('YES')


if __name__ == '__main__':
    main()
