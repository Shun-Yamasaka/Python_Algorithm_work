"""
お釣りの金額を求めるプログラム3
不正入力に対する対策を実施
"""

import sys

input_price = input('insert:')
if not input_price.isdecimal():
    print('整数を入力してください')
    sys.exit() # エラーがあれば強制終了

product_price = input('product:')
if not product_price.isdecimal():
    print('整数を入力してください')
    sys.exit() # エラーがあれば強制終了

change = int(input_price) - int(product_price)

if change < 0:
    print('金額が不足しています')
    sys.exit() # エラーがあれば強制終了

coin = [5000, 1000, 500, 100, 50, 10 , 5, 1]

for ii in coin:
    re = change // ii
    change %= ii
    print(str(ii) + ':' + str(re))
