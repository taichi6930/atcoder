n = int(input())
aList = list(input().split())
print("YES" if len(aList) == len(set(aList)) else "NO")
