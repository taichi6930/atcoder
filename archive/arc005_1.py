def main():
    n = int(input())
    print(list(map(lambda x: x.lower().replace(
        '.', ''), list(map(str, input().split())))).count('takahashikun'))


if __name__ == '__main__':
    main()
