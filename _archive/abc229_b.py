def main():
    A, B = map(str, input().split())

    for i in range(1, min(len(A), len(B)) + 1):
        x = int(A[-i])
        y = int(B[-i])
        if x + y >= 10:
            print("Hard")
            return

    print("Easy")


if __name__ == '__main__':
    main()
