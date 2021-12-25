# print(0b101)
# print(bin(5))

a = 0b10101

for i in range(5):
    print(a >> i & 1)
