def main():
    sx, sy, gx, gy = map(int, input().split())
    print(sx - sy*(sx - gx) / (sy + gy))


if __name__ == '__main__':
    main()
