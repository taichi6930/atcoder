def main():
    d, t, s = map(int, input().split())
    if s * t >= d:
        print("Yes")
        return
    print("No")


if __name__ == '__main__':
    main()
