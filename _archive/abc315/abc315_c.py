from collections import defaultdict

n = int(input())
FS = [list(map(int, input().split())) for _ in range(n)]

ans = 0

# FをKeyにして、SをValueにした辞書FSDicを作成、Fは重複するので、Valueはリストにする
FSDic = defaultdict(list)
for F, S in FS:
    FSDic[F].append(S)

# FSDicのそれぞれのKeyのValueの1番大きい数字 + 2番目に大きい数字 * 0.5の合計を出力する
for F in FSDic.keys():
    SList = FSDic[F]
    SList.sort(reverse=True)
    if len(SList) <= 1:
        continue
    ans = max(SList[0] + SList[1] * 0.5, ans)


# FSDicのそれぞれのKeyのValueの1番大きい数字を取得したリストFSMaxListを作成
FSMaxList = []
for F, SList in FSDic.items():
    FSMaxList.append(max(SList))

print(
    ans if len(FSMaxList) <= 1 else max(ans, sum(sorted(FSMaxList, reverse=True)[0:2]))
)
