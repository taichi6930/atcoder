path = '/Users/taichi/Documents/atcoder/makestr.txt'

s = 'New file'

with open(path, mode='w') as f:
    # for i in range(100000):
    #     f.write(str(i) + ",")

    for i in range(10000):
        print(i, end=', ')
