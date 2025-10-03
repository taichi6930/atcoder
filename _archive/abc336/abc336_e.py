n = input()


def str2intWithArray(Array):
    return list(map(lambda x: int(x), Array))


listN = str2intWithArray(list(n))
print(listN)
