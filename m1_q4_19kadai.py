# リストを作成
a = [1, 2, 3, 4]

# 変数aのidをid_aに保存
id_a = id(a)

# aをコピーして別オブジェクトを作成
b = a.copy()

# bのidをid_bに保存
id_b = id(b)

# idの比較
if id_a == id_b:
    result = 'A'
elif id(a) == id(b):
    result = 'B'
elif id_a == id(a):
    # id_a には id(a) を代入しているので、必ずここが真になる
    result = 'C'
else:
    result = 'D'

# 判定結果を表示
print(result)

# aのidを表示
print(id(a))

# id_aの中身を表示（id(a)と同じになる）
print(id_a)

# id_aの型を表示
print(type(id_a))

