import collections


def main():
    n = int(input())
    S = list(input())
    A = collections.deque([])

    for i in range(n):
        s = S[i]
        if s == 'L':
            A.appendleft(i + 1)
        elif s == 'R':
            A.append(i + 1)
        elif s == 'A':
            if len(A) <= 0:
                print('ERROR')
                continue
            print(A[0])
            A.remove(A[0])
            continue
        elif s == 'B':
            if len(A) <= 1:
                print('ERROR')
                continue
            print(A[1])
            u = A.popleft()
            A.popleft()
            A.appendleft(u)
            continue
        elif s == 'C':
            if len(A) <= 2:
                print('ERROR')
                continue
            print(A[2])
            t = A.popleft()
            u = A.popleft()
            A.popleft()
            A.appendleft(u)
            A.appendleft(t)
            continue
        elif s == 'D':
            if len(A) <= 0:
                print('ERROR')
                continue
            print(A[-1])
            A.pop()
            continue
        elif s == 'E':
            if len(A) <= 1:
                print('ERROR')
                continue
            print(A[-2])
            t = A.pop()
            A.pop()
            A.append(t)
            continue
        elif s == 'F':
            if len(A) <= 2:
                print('ERROR')
                continue
            print(A[-3])
            t = A.pop()
            u = A.pop()
            A.pop()
            A.append(u)
            A.append(t)
            continue


if __name__ == '__main__':
    main()
