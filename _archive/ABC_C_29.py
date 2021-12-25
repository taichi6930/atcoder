def Base_10_to_n(X, n):
    if (int(X/n)):
        return Base_10_to_n(int(X/n), n)+str(X % n)
    return str(X % n)


n = int(input())
for i in range(3**n):
    num = ('{:0' + str(n) + '}').format(int(Base_10_to_n(i, 3)))
    num = num.replace('0', 'a').replace('1', 'b').replace('2', 'c')
    print(''.join(num))
