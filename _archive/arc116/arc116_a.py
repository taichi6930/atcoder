def main():
    k = int(input())
    for i in range(k):
        n = int(input())
        if n % 2 != 0:
            print("Odd")
            continue
        if n % 4 == 0:
            print("Even")
            continue
        print("Same")


if __name__ == '__main__':
    main()
