import math


def main():
    a, v = map(int,  input().split())
    b, w = map(int,  input().split())
    t = int(input())
    if v <= w:
        print('NO')
        return
    print('YES' if abs(b - a) / (v - w)
          <= t else 'NO')


if __name__ == '__main__':
    main()
