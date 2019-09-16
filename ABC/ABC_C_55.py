n, m = map(int, input().split())
print(n+(m-n*2)//4 if n*2 <= m else m//2)
