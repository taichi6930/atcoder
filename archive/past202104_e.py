def main():
    n = int(input())
    S = list(input())
    A = []

    for i in range(n):
        s = S[i]
        if s == 'L':
            A = [i + 1] + A
        elif s == 'R':
            A = A + [i + 1]
        elif s == 'A':
            if len(A) <= 0:
                print('ERROR')
                continue
            print(A[0])
            A = A[1:]
            continue
        elif s == 'B':
            if len(A) <= 1:
                print('ERROR')
                continue
            print(A[1])
            A = A[0:1] + A[2:]
            continue
        elif s == 'C':
            if len(A) <= 2:
                print('ERROR')
                continue
            print(A[2])
            A = A[0:2] + A[3:]
            continue
        elif s == 'D':
            if len(A) <= 0:
                print('ERROR')
                continue
            print(A[-1])
            A = A[0:-1]
            continue
        elif s == 'E':
            if len(A) <= 1:
                print('ERROR')
                continue
            print(A[-2])
            A = A[0:-2] + A[-1:]
            continue
        elif s == 'F':
            if len(A) <= 2:
                print('ERROR')
                continue
            print(A[-3])
            A = A[0:-3] + A[-2:]
            continue


if __name__ == '__main__':
    main()
