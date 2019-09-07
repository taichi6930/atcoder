n = int(input())
s = sorted(list(map(int, input().split())), reverse=True)
print(s)
string = "Yes"
for i in range(n-1):
    print(s[2**(i)-1], s[2**(i+1)-1], s[2**(i + 1) - 1], s[2**(i + 2) - 1])
    if s[n**(i)-1] > s[n**(i+1)-1] and s[n**(i + 1) - 1] > s[n**(i + 2) - 1]:
        string = "Yes"
    else:
        string = "No"
        break

print(string)
