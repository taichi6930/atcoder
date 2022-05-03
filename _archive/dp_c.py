n = int(input())

ABC = [[0 for _ in range(3)] for _ in range(n)]
ABC[0] = list(map(int, input().split()))

for i in range(1, n):
    newabc = list(map(int, input().split()))
    oldabc = ABC[i - 1]

    ABC[i] = [max(oldabc[(j + 1) % 3], oldabc[(j + 2) % 3]) + newabc[j]
              for j in range(3)]

print(max(ABC[-1]))
