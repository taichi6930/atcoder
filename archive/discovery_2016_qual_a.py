def main():
    s = "DiscoPresentsDiscoveryChannelProgrammingContest2016"
    w = int(input())

    for i in range(51):
        if w * (i) >= len(s):
            return
        print(s[i * w: min((i + 1) * w, len(s))])


if __name__ == '__main__':
    main()
