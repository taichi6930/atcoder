from itertools import accumulate
n, l, r = map(int, input().split())
A = tuple(map(int, input().split()))
accA = [0] + list(accumulate(A))

l_list, r_list = [0], [0]

for i in range(n):
    l_list.append(l_list[-1] + A[i] - l)
    r_list.append(r_list[-1] + A[n - i - 1] - r)

r_list = r_list[::-1]

l_max_index = l_list.index(max(l_list))
r_max_index = r_list.index(max(r_list))

# print(l_max_index, l_list)
# print(r_max_index, r_list, r_list[r_max_index:])
# print(accA)

if l_max_index < r_max_index:
    exit(print(
        l_max_index * l + (n - r_max_index) * r +
        accA[r_max_index] - accA[l_max_index]
    ))

r_list_1 = r_list[l_max_index + 1:]
r_max_index_1 = r_list_1.index(max(r_list_1)) + l_max_index + 1

l_list_1 = l_list[:r_max_index + 1]
l_max_index_1 = l_list_1.index(max(l_list_1))

print(
    min(
        l_max_index * l + (n - r_max_index_1) * r +
        accA[r_max_index_1] - accA[l_max_index],
        l_max_index_1 * l + (n - r_max_index) * r +
        accA[r_max_index] - accA[l_max_index_1]
    )
)
