import collections


def main():
    n = int(input())
    L = sorted(list(map(int, input().split())))
    counter = collections.Counter(L)
    keys = list(counter.keys())
    lenKeys = len(keys)
    if lenKeys < 3:
        print(0)
        return
    cnt = 0
    for a in range(lenKeys - 2):
        for b in range(a + 1, lenKeys - 1):
            for c in range(b + 1, lenKeys):
                if keys[a] + keys[b] > keys[c]:
                    cnt += counter[keys[a]] * \
                        counter[keys[b]] * counter[keys[c]]
    print(cnt)


if __name__ == '__main__':
    main()
