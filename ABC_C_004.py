N = int(input()) % 30
X = ["1", "2", "3", "4", "5", "6"]
for j in range(N):
    j = j % 5
    X[j], X[j + 1] = X[j+1], X[j]
print("".join(X))
