# W = list(input())
# word = ""
# for st in W:
#     if not (st == "a" or st == "i" or st == "u" or st == "e" or st == "o"):
#         word += st
# print(word)

W = input()
bo = ['a', 'i', 'u', 'e', 'o']
for i in bo:
    W = W.replace(i, '')
print(W)
