s = input()
c = s.count
r = abs(c("R") - c("L")) + abs(c("U") - c("D"))
q = c("?")
k = r - q
print(r + q if int(input()) == 1 else k if k >= 0 else - k % 2)
