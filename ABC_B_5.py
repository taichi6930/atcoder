# たこ焼きの個数を取得
N = int(input())

# たこ焼きの置かれている時間の最小値を設定
minNum = 100

# たこ焼きの出来る回数だけ回す
for i in range(N):

    # たこ焼きの置かれている時間を取得
    finTime = int(input())

    # たこ焼きの置かれている時間が最小だった場合
    if finTime < minNum:

        # 記録を更新
        minNum = finTime

# 結果を出力
print(minNum)
