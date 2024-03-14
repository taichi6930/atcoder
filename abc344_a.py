import re

a = re.split(r"\|", "1" + input() + "1")
print((a[0] + a[-1]).replace("1", ""))
