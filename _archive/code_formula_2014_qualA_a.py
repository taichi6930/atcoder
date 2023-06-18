
def main():
    n = int(input())
    for i in range(100):
        if (i + 1) ** 3 == n:
            print("YES")
            return
    print("NO")


if __name__ == '__main__':
    main()
