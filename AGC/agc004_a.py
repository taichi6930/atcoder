abcList = list(map(int, input().split()))
print((sum(abcList) - max(abcList) - min(abcList))
      * min(abcList) * (max(abcList) % 2))
