# ① == と is の違いについて確認するコード

a = [1, 2, 3]
b = [1, 2, 3]
c = a + b

# == は「値が同じか」を比較
print("a == b の結果:", a == b)     # True（値が同じ）

# is は「同じオブジェクト（同じメモリ）か」を比較
print("a is b の結果:", a is b)     # False（別々のリスト）

# 実際のメモリアドレスも確認
print("id(a):", id(a))
print("id(b):", id(b))


# ② bool(a is b) が True になる例
# b に a の参照を代入すると、同じオブジェクトになる
x = [10, 20, 30]
y = x   # x と y は同じリストを指す

print("\n--- a is b が True になる例 ---")
print("x is y の結果:", x is y)       # True
print("bool(x is y) の結果:", bool(x is y))  # True

# メモリアドレスも同じ
print("id(x):", id(x))
print("id(y):", id(y))



