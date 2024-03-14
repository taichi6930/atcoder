a, b = map(int, input().split())
print(
    "Yes"
    if [a, b]
    in [
        [1, 2],
        [2, 3],
        [4, 5],
        [5, 6],
        [7, 8],
        [8, 9],
    ]
    else "No"
)
