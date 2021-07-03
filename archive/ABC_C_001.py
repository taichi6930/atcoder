import math

Dig, Dis = map(int, input().split())
Dig += 112.5
print(((Dig / 225) % 3600)/10)
Dis = math.ceil(Dis/6)/10
print(Dis)
windPower = 0
windDirection = ""

# 風力
windPowerList = [0, 0.3, 1.6, 3.4, 5.5, 8, 10.8,
                 13.9, 17.2, 20.8, 24.5, 28.5, 32.7, 7200000]
for wp in range(len(windPowerList)):
    if Dis < windPowerList[wp]:
        windPower = wp - 1
        break

# 風向
if windPower == 0:
    windDirection = ""

print(windDirection, windPower)
