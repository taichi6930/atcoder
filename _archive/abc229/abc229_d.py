S = list(input())
k = int(input())
dic = {'.': 0, 'X': 0}

st, gl = 0, 0

ans = 0

for i in range(10 ** 7):
    dic[S[gl]] += 1
    if dic['.'] <= k:
        ans = max(ans, gl - st + 1)
    else:
        dic[S[st]] -= 1
        st += 1
    gl += 1
    if gl >= len(S):
        break
print(ans)
