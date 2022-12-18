S = input()
T = input()

if len(T) < len(S):
    exit(print('No'))

print('Yes' if S == T[:len(S)] else 'No')
