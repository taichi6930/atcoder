def main():
    print("Yes" if "".join(sorted(["H", "2B", "3B", "HR"])) == "".join(
        sorted([input() for _ in range(4)])) else "No")


if __name__ == '__main__':
    main()
