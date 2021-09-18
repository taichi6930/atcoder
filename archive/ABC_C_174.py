

def main():
    k = int(input())
    a = 0
    ans = -1
    for i in range(1, 2 * 10 ** 6):
        a = 10 * a + 7
        a %= k
        if a == 0:
            ans = i
            break
    print(ans)


if __name__ == '__main__':
    main()
