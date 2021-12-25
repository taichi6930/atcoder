def main():
    # print(" ".join(list(map(lambda x: "<" if x == "Left" else ">" if x ==
    #       "Right" else "A", list(map(str, input().split()))))))
    print(" ".join(
        list(map(str, input().split())))
        .replace("Left", "<")
        .replace("Right", ">")
        .replace("AtCoder", "A"))


if __name__ == '__main__':
    main()
