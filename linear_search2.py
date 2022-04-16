# 線形探索を行う関数を作成してみる
def linear_search(data, value): # リストから求める値の位置を検索する関数を定義
    for ii in range(len(data)):
        if data[ii] == value: # 欲しい値が見つかった場合
            return ii
    return -1 # 欲しい値が見つからなかった場合

# 関数を実行
data = [50, 30, 90, 10, 20, 70, 60, 40, 80]
print(linear_search(data, 40)) # データリストと検索値を渡す