def main():
    n = int(input())
    A = sorted([int(input()) for _ in range(n)], reverse=True)

    ansArr = []

    Ah = A[:(n + 1) // 2]
    At = list(reversed(A[(n + 1) // 2:]))
    for i in range(n):
        if len(ansArr) < 2:
            ansArr += [Ah[i]] + [At[i]]
            continue

        if len(Ah) < i+1:
            break
        if abs(Ah[i] - ansArr[0]) >= abs(Ah[i] - ansArr[-1]):
            ansArr = [Ah[i]] + ansArr
        else:
            ansArr = ansArr + [Ah[i]]

        if len(At) < i + 1:
            break

        if abs(At[i] - ansArr[0]) >= abs(At[i] - ansArr[-1]):
            ansArr = [At[i]] + ansArr
        else:
            ansArr = ansArr + [At[i]]

    print(ansArr)


if __name__ == '__main__':
    main()
