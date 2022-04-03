# フィボナッチ数列をプログラムで求める
def fibonacci(n):
    if (n == 1) or (n == 2):
        return 1
    return fibonacci(n - 2) + fibonacci(n - 1) # 関数の中で関数を呼び出す（再帰）

print(fibonacci(7))