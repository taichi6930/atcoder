def cal(i):
    return sum(w[i:n]) - sum(w[0:i])


n = int(input())
w = list(map(int, input().split()))
minNum = 100000
wSum = sum(w)
for i in range(n):
    if cal(i) <= 0:
        print(min(abs(cal(i)), abs(cal(i-1))))
        break
