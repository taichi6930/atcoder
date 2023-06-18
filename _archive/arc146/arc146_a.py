def int2strWithArray(Array):
    return list(map(lambda x: str(x), Array))


n = int(input())
A = int2strWithArray(sorted(list(map(int, input().split())), reverse=True)[:3])
print(max(
    int(A[0] + A[1] + A[2]),
    int(A[0] + A[2] + A[1]),
    int(A[1] + A[0] + A[2]),
    int(A[1] + A[2] + A[0]),
    int(A[2] + A[0] + A[1]),
    int(A[2] + A[1] + A[0]),
))
