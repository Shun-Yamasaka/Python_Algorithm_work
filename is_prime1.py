"""
素数を判定するプログラム
"""
import math # 平方根を扱うため数学モジュールを読み込む

def is_prime(n):
    if n <= 1:
        return False
    for ii in range(2, int(math.sqrt(n)) + 1):
        if n % ii == 0: # 割り切れるか判定
            return False # 割り切れれば素数ではない

    return True # いずれの数でも割り切れなかった時は素数

for i in range(200):
    if is_prime(i):
        print(i, end=' ')