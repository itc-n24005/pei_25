# list_a を作成
list_a = [5, 12, 7, 12, 20]

# list_a を copy() して list_b を作成
list_b = list_a.copy()

# list_b から 12 を1つだけ削除
list_b.remove(12)

# インデックス2の位置に 99 を挿入
list_b.insert(2, 99)

# 末尾に 0 を追加
list_b.append(0)

# 結果を表示
print("list_a:", list_a)
print("list_b:", list_b)

