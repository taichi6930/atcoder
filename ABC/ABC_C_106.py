s = input()
k = int(input())
if s[0] != "1":
  print(s[0])
else:
  s = s[0:k].replace("1", "")
  if len(s) != 0:
    print(s[0])
  else:
    print(1)