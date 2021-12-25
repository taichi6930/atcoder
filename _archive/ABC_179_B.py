n = int(input())
cnt = 0
string = "No"
for i in range(n):
    a, b = map(int, input().split())
    if a != b:
        cnt = 0
        continue
    cnt += 1
    if cnt >= 3:
        string = "Yes"
print(string)
