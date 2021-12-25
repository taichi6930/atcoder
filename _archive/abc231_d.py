def main():
    n, m = map(int, input().split())
    ans = 'Yes'
    okList = [[] for _ in range(n + 1)]
    ngList = [[] for _ in range(n + 1)]

    for i in range(m):
        a, b = map(int, input().split())

        # 互いの連結が出来るかどうかを見に行く（NGLISTにあるかどうか）
        if ngList[a].count(b) > 0 or ngList[b].count(a) > 0:
            ans = 'No'
            continue

        # そもそも連結が出来るか、2つ埋まってないかを見に行く（OKLISTの数を見る）
        if len(okList[a]) >= 2 or len(okList[b]) >= 2:
            ans = 'No'
            continue

        # NGLIST,OKLISTの更新
        okList[a].append(b)
        okList[b].append(a)
        ngList[a] = ngList[a] + okList[b]

    print(ans)


if __name__ == '__main__':
    main()
