def main():
    n = input()
    print("YNeos"[not(n[0] == "7" or n[1] == "7" or n[2] == "7")::2])


if __name__ == '__main__':
    main()
