def main():
    a, b = map(int, input().split())
    if a + b == 15:
        print("+")
        return
    if a * b == 15:
        print("*")
        return
    print("x")


if __name__ == '__main__':
    main()
