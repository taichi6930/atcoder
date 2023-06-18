S = list(map(str, input().split()))
T = list(map(str, input().split()))

x, y, z = S[0], S[1], S[2]

if ((T[0] == x and T[1] == y and T[2] == z)
    or (T[0] == y and T[1] == z and T[2] == x)
        or (T[0] == z and T[1] == x and T[2] == y)):
    print('Yes')
else:
    print('No')
