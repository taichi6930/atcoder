N = 45**2 - int(input())
for i in range(9):
    if (N % (i + 1) == 0) & (N // (i + 1) < 10):
        print(i+1, "x", N // (i + 1))
