t = int(input())
Cases = [int(input()) for _ in range(t)]

# 桁数による配列
K = [0]

for i in range(1, 100):
    K.append(9**i + K[-1])

for case in Cases:
    for i, k in enumerate(K):
        # 何桁かが判定できる
        if k > case:
            P = [case // K[i - 1]]
            case -= K[i - 1] * P[0]
            for j in range(2, i):
                p = case // K[i - j]
                P.append(p)
                case -= K[i - j] * p
            P.append(case)
            print(P)
            break
