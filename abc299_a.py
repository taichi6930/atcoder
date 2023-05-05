n = int(input())
S = input()
a = S.rfind("|")
b = S.find("|")
c = S.find("*")

print("oiunt"[(b < c and c < a) :: 2])
