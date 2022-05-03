n, x, y = map(int, input().split())
A = list(map(int, input().split()))

ALeftMin = [A[0]] + [0 for _ in range(n - 1)]
ARightMin = [0 for _ in range(n - 1)] + [A[-1]]
ALeftMax = [A[0]] + [0 for _ in range(n - 1)]
ARightMax = [0 for _ in range(n - 1)] + [A[-1]]

for i in range(n - 1):
    ALeftMin[i + 1] = min(ALeftMin[i], A[i + 1])
    ALeftMax[i + 1] = max(ALeftMax[i], A[i + 1])
    ARightMin[n - (i + 1) - 1] = min(ARightMin[n -
                                               (i + 1)], A[n - (i + 1) - 1])
    ARightMax[n - (i + 1) - 1] = max(ARightMax[n -
                                               (i + 1)], A[n - (i + 1) - 1])

ALeftMin = [0] + ALeftMin + [10 ** 7]
ARightMin = [0] + ARightMin + [10 ** 7]
ALeftMax = [0] + ALeftMax + [10 ** 7]
ARightMax = [0] + ARightMax + [10 ** 7]
print(ALeftMin, ARightMin,  ALeftMax, ARightMax)
