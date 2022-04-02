"""
FizzBuzzを実装してみる。
1~100までの順に出力するプログラムを実装すること。
ただし、3の倍数の時は数の代わりに「Fizz」を
5の倍数の時は「Buzz」を
3と5の両方の倍数の場合には「FizzBuzz」を出力するものとする。
"""
for i in range(1, 101):
    if (i % 3 == 0) and (i % 5 == 0):
        print('FizzBuzz', end=' ')
    elif (i % 3 == 0):
        print('Fizz', end=' ')
    elif (i % 5 == 0): # 5で割り切れるか
        print('Buzz', end=' ')
    else:
        print(i, end=' ')