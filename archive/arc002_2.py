import datetime


def main():
    y, m, d = map(int, input().split('/'))
    k = datetime.datetime(y, m, d)
    for i in range(500):
        if k.year % (k.month * k.day) == 0:
            print(str(k.year) + '/' + '{:002}'.format(k.month) +
                  '/' + '{:002}'.format(k.day))
            return

        k = k + datetime.timedelta(days=1)


if __name__ == '__main__':
    main()
