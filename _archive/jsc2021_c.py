import math


def main():
    a, b = map(int, input().split())
    ans = 0
    for i in range(1, 200001):
        aa = math.ceil(a / i)
        bb = math.floor(b / i)

        if bb > aa:
            ans = i
    print(ans)


if __name__ == '__main__':
    main()
