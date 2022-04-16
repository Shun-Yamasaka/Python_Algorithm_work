# 線形探索について
data = [50, 30, 90, 10, 20, 70, 60, 40, 80] # 探索対象のデータリスト
found = False # 処理状況を管理する（初期値はFalse）
for ii in range(len(data)):
    if data[ii] == 40: # 見つけた値と一致したか？
        print(ii)
        found = True # 見つかったことを処理状況としてセット
        break

if not found: # 見つからなかったとき
    print('Not Found')