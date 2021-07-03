import sys
S = list(input())
T = list(input())

def choose(A,i):
    atcoder = ["a", "t", "c", "o", "d", "e", "r"]
    senser = "NG"
    for ac in atcoder:
        if A[i] == ac:
            senser = "OK"
            return
    print("You will lose")
    sys.exit()



for i in range(len(S)):
    if not S[i] == T[i]:
        # Sの方が@の場合
        if(S[i] == "@"):
            choose(T,i)    
        # Tの方が@の場合
        elif(T[i] == "@"):
            choose(S,i)
        else:
            print("You will lose")
            sys.exit()            

print("You can win")
