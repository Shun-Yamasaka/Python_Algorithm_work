# 通りがけ順の深さ優先探索(再帰で実装)

tree = [[1,2],[3,4],[5,6],[7,8],[9,10],[11,12],[13,14],[],[],[],[],[],[],[],[]]

def search(pos):
    if len(tree[pos]) == 2: # 子が2つある時
        search(tree[pos][0])
        print(pos, end=' ') # 左のノードと右のノードの間に出力
        search(tree[pos][1])
    elif len(tree[pos]) == 1: # 子が1つのとき
        search(tree[pos][0])
        print(pos, end=' ') # 左のノードを調べた後に出力
    else:
        print(pos, end=' ')

search(0)