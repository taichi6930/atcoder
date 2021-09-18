
def main():
    x, k, d = map(int, input().split())
    a = abs(x) - k * d
    if a >= 0:
        print(a)
        return
    if(k - (abs(x) // d)) % 2 == 0:
        print(abs(x) % d)
        return
    print(abs(d - abs(x) % d))
    return


if __name__ == '__main__':
    main()
