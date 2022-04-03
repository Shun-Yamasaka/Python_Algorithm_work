n = 18

# 基数を指定して変換できる関数を作成
def convert(n, base):
    result = ''
    while n > 0:
        result = str(n % base) + result
        n //= base

    return result

print(convert(n, 2)) # 2進数に変換
print(convert(n, 3)) # 3進数に変換
print(convert(n, 8)) # 8進数に変換
