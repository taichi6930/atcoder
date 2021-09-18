def main():
    n = int(input())
    ngList = [int(input()) for _ in range(3)]

    if n in ngList:
        print("NO")
        return
    ans = 0
    for _ in range(100):
        swi = 0
        for i in range(3):
            if ans + 3 - i in ngList:
                continue
            ans += 3 - i
            if ans >= n:
                print("YES")
                return
            swi = 1
            break
        if swi == 0:
            print("NO")
            return
    print("YNEOS"[(ans < n)::2])


if __name__ == '__main__':
    main()
