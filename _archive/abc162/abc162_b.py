import math


def main():
    n = int(input())
    allSum = n * (n + 1) // 2
    threeNum = math.floor(n / 3)
    threeSum = 3 * threeNum * (threeNum + 1) // 2
    fiveNum = math.floor(n / 5)
    fiveSum = 5 * fiveNum * (fiveNum + 1) // 2
    bothNum = math.floor(n / 15)
    bothSum = 15 * bothNum * (bothNum + 1) // 2
    print(allSum + bothSum - threeSum - fiveSum)


if __name__ == '__main__':
    main()
