import collections


def int2strWithArray(Array):  # 数字の配列を文字の配列に変換する
    return list(map(lambda x: str(x), Array))

4*2^0.5 =5.65685424949

def main():
    n = int(input())
    ANS = collections.deque()
    for i in range(1000):
        if n == 0:
            break
        if n % 3 == 0:
            pass
        elif n % 3 == 1:
            ANS.append(3 ** i)
            n -= 1
        elif n % 3 == 2:
            ANS.append(- 3 ** i)
            n += 1
        n = n // 3
    print(len(ANS))
    print(' '.join(int2strWithArray(ANS)))


if __name__ == '__main__':
    main()
