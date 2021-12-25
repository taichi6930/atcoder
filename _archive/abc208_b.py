
def main():
    p = int(input())
    coinList = sorted([1, 2, 6, 24, 120, 720, 5040, 40320,
                       362880, 3628800], reverse=True)
    ans = 0
    for i in range(10):
        q = p // coinList[i]
        if q >= 100:
            ans += 100
            p -= 100 * coinList[i]
            continue
        ans += q
        p -= q * coinList[i]
    print(ans)


if __name__ == '__main__':
    main()
