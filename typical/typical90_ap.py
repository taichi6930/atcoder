# def main():
#     k = int(input())

#     if k % 9 != 0:  # kが9の倍数でない場合
#         print(0)
#         return

#     p = [1] * (k + 1)

#     for i in range(1, k):
#         for j in range(min(i, 9)):
#             p[i] = (p[i] + p[i - j]) % (10 ** 9 + 7)

#     print(p)


# if __name__ == '__main__':
#     main()
