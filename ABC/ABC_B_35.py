s = input()
t = int(input())

hor = abs(s.count("R") - s.count("L"))
ver = abs(s.count("U") - s.count("D"))
que = s.count("?")
print(hor, ver)

# まだ途中
