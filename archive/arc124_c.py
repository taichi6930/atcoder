import math


def main():
    n = int(input())
    AB = [list(map(int, input().split())) for i in range(n)]
    AB.sort(key=lambda x: x[1])
    AB.sort(key=lambda x: x[0])
    [A, B] = AB[0]
    print(AB)

    for i in range(1, n):
        a, b = AB[i]
        Aa, Bb = math.gcd(A, a), math.gcd(B, b)
        Ab, Ba = math.gcd(A, b), math.gcd(B, a)

        AaBb = Aa * Bb // math.gcd(Aa, Bb)
        AbBa = Ab * Ba // math.gcd(Ab, Ba)

        if AaBb >= AbBa:
            A, B = Aa, Bb
            continue
        A, B = Ab, Ba

    ans1 = A * B // math.gcd(A, B)
    print(A, B)

    AB.sort(key=lambda x: x[1])
    print(AB)
    [A, B] = AB[0]

    for j in range(1, n):
        a, b = AB[j]
        Aa, Bb = math.gcd(A, a), math.gcd(B, b)
        Ab, Ba = math.gcd(A, b), math.gcd(B, a)

        AaBb = Aa * Bb // math.gcd(Aa, Bb)
        AbBa = Ab * Ba // math.gcd(Ab, Ba)

        if AaBb >= AbBa:
            A, B = Aa, Bb
            continue
        A, B = Ab, Ba

    ans2 = A * B // math.gcd(A, B)
    print(A, B)
    print(max(ans1, ans2))


if __name__ == '__main__':
    main()
