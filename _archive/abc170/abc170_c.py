def main():
    x, n = map(int,  input().split())
    p = list(map(int,  input().split()))
    for k in range(100):
        if p.count(x - k) == 0:
            print(x - k)
            break
        if p.count(x + k) == 0:
            print(x + k)
            break


if __name__ == '__main__':
    main()
