def main():
    h, bmi = map(float, input().split())
    print(bmi * (h / 100) ** 2)


if __name__ == '__main__':
    main()
