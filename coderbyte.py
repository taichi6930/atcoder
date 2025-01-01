from collections import Counter
import ast


def MinWindowSubstring(strArr):
    [N, K] = ast.literal_eval(strArr)

    cK = Counter(K)

    ans = len(N)
    ansNum = 1

    for i in range(len(N)):
        cck = cK.copy()
        for j in range(i, len(N)):
            print(cck, i, j)
            if N[j] in cck:
                cck[N[j]] -= 1
                if cck[N[j]] == 0:
                    cck.pop(N[j])
            if not cck:
                ans = min(ans, j - i + 1)
                ansNum = i

    return N[ansNum - 1 : ansNum + ans - 1]


print(MinWindowSubstring(input()))
