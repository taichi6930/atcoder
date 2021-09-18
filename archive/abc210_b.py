def main():
    n = int(input())
    s = list(input())
    ans = s.index("1")

    print("Takahashi" if ans % 2 == 0 else "Aoki")


if __name__ == '__main__':
    main()
