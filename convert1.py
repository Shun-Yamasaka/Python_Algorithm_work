"""
基数変換を行うプログラム
"""

n = 18

result = ''

# 2進数に変換
while n > 0:
    result = str(n % 2) + result # あまりの文字列の左側に追加していく
    n //= 2 # 2で割った商を再度代入する

print(result)