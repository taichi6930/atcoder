from collections import Counter, deque
s = deque(list(input()))
cnt = 0

for _ in range(10 ** 10):
    if len(s) <= 1:
        break
    if s[0] == s[-1]:
        s.pop()
        s.popleft()
        continue
    if s[0] == 'x':
        cnt += 1
        s.popleft()
        continue
    if s[-1] == 'x':
        cnt += 1
        s.pop()
        continue
    break

print(-1 if len(s) > 1 else cnt)
