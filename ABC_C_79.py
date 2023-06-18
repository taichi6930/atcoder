calcNum = [1, -1]
calcSign = ["+", "-"]
n = list(input())
for a in range(2):
    for b in range(2):
        for c in range(2):
            if int(n[0]) + calcNum[a] * int(n[1]) + calcNum[b] * int(n[2]) + calcNum[c] * int(n[3]) == 7:
                string = n[0] + calcSign[a] + n[1] + \
                    calcSign[b] + n[2] + calcSign[c] + n[3] + "=7"

print(string)
