nStr = input()
nTopNum = int(nStr[0])
nNum = int(nStr)
print(nNum if nNum % 111 == 0 else nTopNum *
      111 if nTopNum * 111 > nNum else (nTopNum + 1) * 111)
