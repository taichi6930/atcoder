ans = 1
for i in range(int(input())):
    ans *= i + 1
    ans %= 10 ** 9 + 7
print(ans)
