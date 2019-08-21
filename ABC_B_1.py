m = int(input())
if m < 100:
    print("00")
elif m < 1000:
    print("0"+str(m//100))
elif m <= 5000:
    print(m//100)
elif m <= 30000:
    print(m//1000+50)
elif m <= 70000:
    print(m/1000+74)
else:
    print(89)
