def main():
    n = int(input())
    aList = sorted(list(map(int,  input().split())))
    z = [0] * n
    for a in aList:
        z[a-1] += 1

    for i in range(n):
        print(z[i])


if __name__ == '__main__':
    main()
