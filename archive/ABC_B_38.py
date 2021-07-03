a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))
sum = 0
for i in range(2):
    if a1[i] == a2[i] or a1[i] == a2[1-i]:
        if sum == 0:
            print("YES")
            sum = 1
if sum == 0:
    print("NO")
