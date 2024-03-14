from itertools import combinations


def lcm_result(numbers):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def lcm(a, b):
        return a * b // gcd(a, b)

    lcm_result = numbers[0]
    for num in numbers[1:]:
        lcm_result = lcm(lcm_result, num)

    return lcm_result


n, k = map(int, input().split())
V = list(map(int, input().split()))

ans = 0

for i in range(1, k + 1):
    C = combinations(V, i)
    for c in C:
        result = lcm_result(c)
        ans += ((-1) ** (i + 1)) * (n // result)

print(ans)
