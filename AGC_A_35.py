def test(a):
    for i in range(0, len(a)-2):
        if((a[i]^a[i+2])!=a[i+1]):
            return "No"

    if((a[len(a)-2]^a[0])!=a[len(a)-1]):
        return "No"
    if((a[len(a)-1]^a[1])!=a[0]):
        return "No"
    if((a[0]^a[2])!=a[1]):
        return "No"
    return "Yes"

N = int(input())
a = list(map(int, input().split()))
print(test(a))
