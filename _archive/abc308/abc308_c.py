n = int(input())
AB = [list(map(int, input().split())) for _ in range(n)]
ABANS = [["{:.40f}".format(a / (a + b)), n - (i + 1)] for i, [a, b] in enumerate(AB)]
print(
    " ".join(
        list(map(lambda x: str(x), [n - ans[1] for ans in sorted(ABANS, reverse=True)]))
    )
)
