def main():
    h, w, k = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if sum(A) % k != sum(B) % k:
        print(-1)
        return

    print(((max(sum(A), sum(B)) + (h + w)) // k) * k + max(sum(A), sum(B)) % k)


if __name__ == '__main__':
    main()
