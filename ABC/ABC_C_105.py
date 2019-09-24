n = int(input())
string = ""

for i in range(10**10):
    if n == 0:
        break
    if n % 2 == 1:
        string = "1" + string
        n -= (-1)**(i)
    else:
        string = "0" + string
    n = n // 2

print(string if string != "" else 0)
