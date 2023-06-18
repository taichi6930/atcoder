def main():
    n, s = map(str, input().split())
    n = int(n)
    t = "" + s
    print(t)

    t = t.replace('A', '1').replace('G', '2').replace('C', '3').replace(
        'T', '4').replace('1', 'T'). replace('2', 'C').replace('3', 'G').replace('4', 'A')
    print(s, t)


if __name__ == '__main__':
    main()
