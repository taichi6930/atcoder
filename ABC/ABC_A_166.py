import sys
readline = sys.stdin.readline


def main():
    print("A" + ("R" if readline().rstrip()[1] == "B" else "B") + "C")


if __name__ == '__main__':
    main()
