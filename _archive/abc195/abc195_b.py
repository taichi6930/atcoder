def main():
    a, b, w = map(int, input().split())
    ansf, ansg = -1, -1
    for i in range(10 ** 7):
        if a * i > 1000 * w:
            break

        if 1000 * w <= b * i:
            ansg = i
            if ansf == -1:
                ansf = i
    print(" ".join([str(ansf), str(ansg)]) if ansf != -
          1 and ansg != -1 else "UNSATISFIABLE")


if __name__ == '__main__':
    main()
