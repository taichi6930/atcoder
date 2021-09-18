
def main():
    a = list(input())
    print(a[(int(input()) % len(a) - 1) % len(a)])


if __name__ == '__main__':
    main()
