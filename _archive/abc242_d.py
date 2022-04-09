s = list(input())
n = len(s)
q = int(input())
alphabet = list('ABC')

tr = {'A': 'BC', 'B': 'CA', 'C': 'AB'}


def f(t, k):
    if t == 0:
        return s[k]
    if k == 0:
        return alphabet[(alphabet.index(s[0]) + t) % 3]
    else:
        return tr[f(t - 1, k // 2)][k % 2]


for _ in range(q):
    t, k = map(int, input().split())
    print(f(t, k - 1))
