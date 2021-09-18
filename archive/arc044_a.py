import math


def is_prime(n):
    if n == 1:
        return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True


def main():
    n = int(input())

    # 素数判定を行う
    if is_prime(n):
        print("Prime")
        return

    # 素数っぽくない条件を出す
    n1 = int(str(n)[-1])
    if n1 % 2 == 0 or n1 == 5 or n == 1:
        print("Not Prime")
        return

    arrayN = list(map(lambda x: int(x),
                      list(str(n))))
    if sum(arrayN) % 3 == 0:
        print("Not Prime")
        return

    print("Prime")


if __name__ == '__main__':
    main()
