for _ in range(int(input())):
    n = int(input())
    print(sum([i % 2 for i in list(map(int, input().split()))]))
