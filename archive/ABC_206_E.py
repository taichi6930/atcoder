def main():
    l, r = map(int, input().split())
    if r == 1:
        print(0)
        return

    for i in range(2, r + 1):
        for j in range(1, r + 1):
            if i * j > r:
                break
            math.gcd()
import math




if __name__ == '__main__':
    main()
