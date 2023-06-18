def k(num):
    if num in p:
        return '.'
    if num in q:
        return 'o'
    return 'x'


a, b = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

print(k(7) + ' ' + k(8) + ' ' + k(9) + ' ' + k(0))
print(' ' + k(4) + ' ' + k(5) + ' ' + k(6) + ' ')
print('  ' + k(2) + ' ' + k(3) + '  ')
print('   ' + k(1) + '   ')
