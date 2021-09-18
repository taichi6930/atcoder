def main():
    n, k = map(int,  input().split())
    P = sorted(list(map(int,  input().split())))
    print(sum(P[0: k]))


if __name__ == '__main__':
    main()
