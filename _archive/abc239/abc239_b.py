import math


def main():
    x = input()
    if x == '0':
        print(0)
        return
    if int(x) > -10 and int(x) < 10:
        print(math.floor(int(x) / 10))
        return
    if x[-1] == '0':
        print(x[0:-1])
        return
    if x[0] != '-':
        print(x[0:-1])
        return
    print(int(x[0:-1]) - 1)


if __name__ == '__main__':
    main()
