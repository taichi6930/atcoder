def main():
    h, w = map(int, input().split())
    B = [[] for _ in range(w)]

    for i in range(h):
        A = list(map(int, input().split()))
        for a in range(len(A)):
            B[a].append(A[a])

    for j in range(w):
        print(" ".join(list(map(lambda x: str(x), B[j]))))


if __name__ == '__main__':
    main()
