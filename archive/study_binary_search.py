import time

my_list = []
start = time.time()
for i in range(20000000):
    my_list.append(i)

goal = time.time()
print("time/ms:", (goal - start))

print("k")


def simple_search(list, item):
    start = time.time()
    for i in list:
        guess = i
        if guess == item:
            goal = time.time()
            print("time/ms:", (goal - start))
            return guess


def binary_search(list, item):
    start = time.time()
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            goal = time.time()
            print("time/ms:", (goal - start))
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None


print(simple_search(my_list, 7777777))
print(binary_search(my_list, 7777777))
