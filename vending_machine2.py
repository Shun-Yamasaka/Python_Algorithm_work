"""
お釣りの金額を求めるプログラム2
リストとループでシンプルな実装に変更
"""

input_price = input('insert:')
product_price = input('product:')
change = int(input_price) - int(product_price)

# 紙幣硬貨のリスト
coin = [5000, 1000, 500, 100, 50, 10, 5, 1]

for ii in coin:
    re = change // ii
    change %= ii
    print(str(ii)+ ':' + str(re))