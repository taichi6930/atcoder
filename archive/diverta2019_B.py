
def main():
    cnt = 0
    R, G, B, N = list(map(int, input().split()))
    for r in range(N // R + 1):
        for g in range((N - r * R)//G + 1):
            if N - r * R - g * G % B == 0:
                cnt += 1
    print(cnt)


if __name__ == '__main__':
    main()
