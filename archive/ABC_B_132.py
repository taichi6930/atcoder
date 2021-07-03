n = int(input())
p_list = list(map(int, input().split()))
cnt = 0
for i in range(1, n-2):
    if((p_list[i-1] > p_list[i] & p_list[i] > p_list[i+1]) | (p_list[i-1] < p_list[i] & p_list[i] < p_list[i+1])):
        cnt += 1
print(cnt)
