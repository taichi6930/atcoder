o, e = [input() for _ in range(2)]
string = ""
for i in range(min(len(o), len(e))):
    string = string + o[i] + e[i]
if len(o) - len(e) == 1:
    string += o[-1]
print(string)
