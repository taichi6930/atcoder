N = int(input())
A_list = [0]

# まずは全ての値を取ってくる
for i in range(N):
    # Aの値を取る
    swi = 0
    A = int(input())
    for j in range(len(A_list)):
        if A > A_list[j]:
            A_list[j] = A
            swi = 1
            break
    if swi == 0:
        A_list.append(A)


print(A_list)
