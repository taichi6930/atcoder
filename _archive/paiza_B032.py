n = int(input())
ans_list = [
    '*|=|****',
    '*|=*|***',
    '*|=**|**',
    '*|=***|*',
    '*|=****|',
    '|*=|****',
    '|*=*|***',
    '|*=**|**',
    '|*=***|*',
    '|*=****|',
]
A = ['' for _ in range(n)]
for _ in range(8):
    a = list(input())
    for i, aa in enumerate(a):
        A[i] += aa

B = ['' for _ in range(n)]
for _ in range(8):
    b = list(input())
    for i, bb in enumerate(b):
        B[i] += bb

a_num = int(''.join([str(ans_list.index(a)) for a in A]))
b_num = int(''.join([str(ans_list.index(b)) for b in B]))

c_num_str = ('0' * n + str(sum([a_num, b_num])))[-1 * n:]

C = [ans_list[int(c)] for c in list(c_num_str)]

for i in range(8):
    s = ''
    for j in range(n):
        s += C[j][i]
    print(s)
