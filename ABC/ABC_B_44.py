w = input()
for i in range(len(w)):
    if len(w) == 0:
        print("Yes")
        break
    if w.count(w[0]) % 2 == 0:
        w = w.replace(w[0], "")
    else:
        print("No")
        break
