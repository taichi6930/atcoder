n = input()
print(
    "Yes" if sum([1 if n.count(str(i)) != i else 0 for i in range(1, 4)]) == 0 else "No"
)
