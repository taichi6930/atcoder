def main():
    x = int(input())
    if x >= 90:
        print('expert')
        return
    if x >= 70:
        print(90 - x)
        return
    if x >= 40:
        print(70 - x)
        return
    print(40 - x)


if __name__ == '__main__':
    main()
