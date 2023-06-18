n = int(input())
s = list(input())
[a, at, atc, atco, atcod, atcode, atcoder] = [0, 0, 0, 0, 0, 0, 0]

for i in s:
    if i == "a":
        a += 1
        continue

    if i == "t":
        at += a
        continue

    if i == "c":
        atc += at
        continue

    if i == "o":
        atco += atc
        continue

    if i == "d":
        atcod += atco
        continue

    if i == "e":
        atcode += atcod
        continue

    if i == "r":
        atcoder += atcode
        continue

print(atcoder % (10 ** 9 + 7))
