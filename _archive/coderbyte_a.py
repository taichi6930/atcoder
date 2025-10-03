# Linux ベースのターミナルで、
# `mkdir -p path/to/directory`のように連続してコマンドを実行し、
# ディレクトリを作成するというシナリオを考えてみよう。
# 最初は、カレントディレクトリの下にファイルやディレクトリがないと仮定する。

# i=0,1,2,...`の文字列パスの配列が与えられたとき、
# ディレクトリパス paths[i]を指定して `mkdir -p` を連続して実行する。
# 各実行に対して、新しく作成されるディレクトリの数を計算せよ。
# どのようなプログラミング言語を使ってもよい。
# ただ、以下の要求に従ってメソッド/関数を実装してください。
# 入力サイズが小さい場合と大きい場合の両方でコードを評価します。コードの時間的複雑さをできるだけ最適化してください。
# 解の時間複雑度はO(sum_i |paths[i]|)であることが期待されます。


def solve(paths: list[str]) -> list[int]:
    # dicはディレクトリ構造を保持する辞書型
    dic = {}
    ans = []
    for path in paths:
        k = 0
        # パスをスラッシュで分割
        splited_paths = path.split("/")
        # aはdicの参照コピー
        temp_dic = dic
        for splited_path in splited_paths:
            # ディレクトリが存在するかを確認
            if splited_path in temp_dic:
                temp_dic = temp_dic[splited_path]
                continue
            # ディレクトリが存在しない場合、新しいディレクトリを作成
            k += 1
            temp_dic[splited_path] = {}
            temp_dic = temp_dic[splited_path]
        ans.append(k)  # 新しく作成されたディレクトリの数を記録

    return ans


paths = ["1234567890/examples", "1234567890/tests", "1234567890/src"]
print(solve(paths))
