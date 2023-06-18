def test(A, B):
    if((A > 0 and A <= 12) and (B > 0 and B <= 12)):
        print("AMBIGUOUS")
        return

    if((B > 0 and B <= 12)):
        print("YYMM")
        return

    if ((A > 0 and A <= 12)):
        print("MMYY")
        return

    print("NA")


S = list(input())
A = int(S[0] + S[1])
B = int(S[2] + S[3])
test(A, B)


# if S[K-1] == "A":
#     S[K-1] = "a"
# if S[K-1] == "B":
#     S[K-1] = "b"
# if S[K-1] == "C":
#     S[K-1] = "c"

# print(''.join(S))
