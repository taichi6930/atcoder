n = int(input())
s = input()
print("YNeos"[not(s[0:n//2] == s[n//2:n] and n % 2 == 0)::2])
