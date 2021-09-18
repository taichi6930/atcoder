def main():
    abc = list(map(int, input().split()))
    print(list('ABC')[abc.index(sum(abc) - max(abc) - min(abc))])


if __name__ == '__main__':
    main()
