import math


def main():

    n = int(input())
    a = math.floor(1.08 * n)
    if a == 206:
        print("so-so")
        return
    if a < 206:
        print("Yay!")
        return
    print(":(")


if __name__ == '__main__':
    main()
