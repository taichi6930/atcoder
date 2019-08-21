engList = [int(input()) for _ in range(3)]
for i in range(3):
    if engList[i] == max(engList):
        print(1)
    elif engList[i] == min(engList):
        print(3)
    else:
        print(2)
