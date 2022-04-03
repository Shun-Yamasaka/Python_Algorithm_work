# 2進数を10進数に変換

n = '10010'

result = 0
for ii in range(len(n)):
    # 1文字ずつ取り出し累乗部分を計算
    result += int(n[ii]) * (2 ** (len(n) - ii - 1))

print(result)
