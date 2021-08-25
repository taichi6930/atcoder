import collections


def main():
    print(collections.Counter(list(input())).most_common()[0][0])


if __name__ == '__main__':
    main()
