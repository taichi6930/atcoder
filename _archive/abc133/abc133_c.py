def exam(L, R):
    min = 2019
    if L-R > 2019:
        return 0
    for i in range(L, R):
        for j in range(i + 1, R + 1):
            modval = i*j % 2019
            if modval < min:
                min = modval
                if min == 0:
                    return 0
    return min


L, R = map(int, input().split())
print(exam(L, R))

# for i in range(L, R+1):
#     for j in range(i + 1, R+1):
#         print(str(i) + "," + str(j))
