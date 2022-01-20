def main():
    n = sorted(list(input()), reverse=True)
    a, b = '', ''
    for i in range(len(n)):
        if i % 4 == 0 or i % 4 == 3:
            a += n[i]
            continue
        b += n[i]
    print(int(a) * int(b))


if __name__ == '__main__':
    main()
