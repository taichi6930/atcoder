n = int(input())
print('YNeos'[
      not (min(1, sum([a in ['and', 'not', 'that', 'the', 'you'] for a in list(map(str, input().split()))])))::2])
