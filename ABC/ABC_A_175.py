import math


def main():
    s = list(input())
    if s.count("R") == 3:
        print(3)
        return
    if s[0] + s[1] == "RR" or s[2] + s[1] == "RR":
        print(2)
        return
    if s.count("R") >= 1:
        print(1)
        return
    print(0)


if __name__ == '__main__':
    main()
