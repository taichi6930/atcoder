# inputList = []
# for i in range(0, 4):
#     inputList.append(input().split(" "))

# for a in range(0, 4):
#     for b in range(0, 2):
#         inputList[a][b], inputList[3 - a][3 -
#                                           b] = inputList[3 - a][3 - b], inputList[a][b]

# for i in range(0, 4):
#     output = ""
#     for j in range(0, 4):
#         output += inputList[i][j] + " "
#     print(output)

# c = reversed([reversed(list(input().split())) for i in range(1)])
# for i in c:
#     print(" ".join(i))

a = list(input().split())
print(a)
a.reverse()
print(a)
