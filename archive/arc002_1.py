def main():
    y = int(input())
    print("YES" if (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0) else "NO")


if __name__ == '__main__':
    main()
