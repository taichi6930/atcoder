
from bisect import bisect_left


def main():
    n = int(input())
    ans = []
    for i in range(n):
        w = int(input())
        if len(ans) == 0:
            ans.append(w)
            continue
        index = bisect_left(ans, w)
        if len(ans) == index:
            ans.append(w)
            continue
        ans[index] = w

    print(len(ans))


if __name__ == '__main__':
    main()
