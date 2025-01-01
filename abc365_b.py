n = int(input())
A = list(map(int, input().split()))
sortedA = sorted(A)

# sortedAの中で2番目に大きい要素を取得
k = sortedA[-2]
# Aの中でkが何番目かを取得
print(A.index(k) + 1)
