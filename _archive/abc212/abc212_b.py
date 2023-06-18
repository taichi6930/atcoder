def main():
    X = input()
    A = "0123456789012"
    Alis = [A[i: i + 4] for i in range(10)]

    # 最初のパターンを調べる
    if X[0] == X[1] and X[2] == X[1] and X[2] == X[3]:
        print("Weak")
        return

    # 2つ目のパターンを調べる
    if Alis.count(X) > 0:
        print("Weak")
        return

    print("Strong")


if __name__ == '__main__':
    main()
