n = int(input())
H = list(map(int, input().split()))

from collections import defaultdict

dict = defaultdict(list)

for i, h in enumerate(H):
    dict[h].append(i)

for key, value in dict.items():
    value.sort()
    max_length = 1
    current_length = 1
    for i in range(1, len(value)):
        if value[i] - value[i - 1] == value[1] - value[0]:
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 1
    max_length = max(max_length, current_length)
    print(f"Value: {key}, Max Arithmetic Subsequence Length: {max_length}")
