def main():
    n = int(input())
    A = [list(map(int,  input().split())) for _ in range(n)]
    A.sort(key=lambda x: x[1])
    sumTime = 0
    maxTime = 0
    for arr in A:
        maxTime = arr[1]
        sumTime += arr[0]
        if maxTime - sumTime < 0:
            print("No")
            return
    print('Yes')


if __name__ == '__main__':
    main()
