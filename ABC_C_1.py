import math

deg, dis = map(int, input().split())
disList = [0, 0.3, 1.6, 3.4, 5.5, 8, 10.8, 13.9, 17.2, 20.8, 24.5, 28.5, 32.7]
degList = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE",
           "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
print(math.floor((deg - 112.5)/220))
# k = math.ceil((deg + 112.5) / 220)
# print(degList[k])
# dis = int((int(dis / 60 * 100))/10)
# print(dis)
# for i in range(len(disList)):
#     if disList[i] >= dis:
#         print(i - 1)
#         break
