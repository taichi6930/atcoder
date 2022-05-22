from decimal import Decimal, ROUND_HALF_UP
deg, dis = map(int, input().split())
degList = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE',
           'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']
disList = [0, 0.3, 1.6, 3.4, 5.5, 8, 10.8, 13.9, 17.2, 20.8, 24.5, 28.5, 32.7]

deg += 112.5

w = 12

b = Decimal(str(dis / 6)).quantize(Decimal('1'), rounding=ROUND_HALF_UP)

for i in range(len(disList) - 1):
    if disList[i] * 10 <= b < disList[i + 1] * 10:
        w = i
        break

dir = degList[int(deg / 3600 * 16) % 16] if w != 0 else 'C'

print(dir, w)
