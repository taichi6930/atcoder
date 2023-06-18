n, k = map(int, input().split())
S = input()
T = ''

for i in range(n):
    if S[i] == 'x' or k == 0:
        T += 'x'
        continue
    k -= 1
    T += 'o'

print(T)
