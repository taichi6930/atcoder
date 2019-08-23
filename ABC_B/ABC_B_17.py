x = input()


if len(x) == 1:
    if x == "o" | x == "k" | x == "u":
        print("YES")
else:
    for i in range(len(x)-1):
        print(x)
