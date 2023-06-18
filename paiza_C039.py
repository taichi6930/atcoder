from collections import Counter
cs = Counter(list(input()))

print(cs['/'] + cs['<'] * 10)
