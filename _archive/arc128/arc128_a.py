from collections import *
n = int(input())
A = list(map(int, input().split()))

Gold = [1]
Silver = [0]

for i in range(n):
    oldGold = Gold[-1]
    oldSilver = Silver[-1]
    