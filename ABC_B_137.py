K, X = map(int, input().split())
string = ""
for i in range(X-K+1, X+K):
    string += str(i) + " "
print(string)
