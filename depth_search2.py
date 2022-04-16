# 深さ優先探索（帰りがけ順）
tree = [[1,2],[3,4],[5,6],[7,8],[9,10],[11,12],[13,14],[],[],[],[],[],[],[],[]]

def search(pos):
    for ii in tree[pos]:
        search(ii)
    print(pos, end=' ') # 配下のノードを調べた後に出力

search(0)