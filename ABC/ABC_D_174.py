
import collections


def main():
    n = int(input())
    c = list(input())
    wcnt = c.count("W")
    rcnt = c.count("R")
    if wcnt == 0 or rcnt == 0:
        print(0)
        return
    ans = c[0:rcnt].count("W")
    print(ans)


if __name__ == '__main__':
    main()
