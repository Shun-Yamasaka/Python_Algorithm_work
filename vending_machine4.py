# divmod関数の例（商とあまりを対で返す）
input_price = input('insert:')
product_price = input('product:')
change = int(input_price) - int(product_price)

coin = [5000, 1000, 500, 100, 50, 10, 5, 1]

for ii in coin:
    re, change = divmod(change, ii)

    print(str(ii) + ':' + str(re))