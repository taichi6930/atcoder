import datetime
y, m, d = [int(input()) for _ in range(3)]
fy, fm, fd = [2014, 5, 17]
# sdate = datetime.date(y, m, d)
# fdate = datetime.date(fy, fm, fd)
# print((fdate - sdate).days)
if m < 3:
    y -= 1
    m += 12

s1 = 365 * y + int(y / 4) - int(y / 100) + int(y / 400) + \
    int(306 * (m + 1) / 10) + d - 429
s2 = 365 * fy + int(fy / 4) - int(fy / 100) + int(fy / 400) + \
    int(306 * (fm + 1) / 10) + fd - 429
print(s2 - s1)
