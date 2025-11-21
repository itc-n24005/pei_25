def func(a, b):
    # a ** b（a の b 乗）が 64 以下なら 1 を返し、それ以外は 0 を返す関数
    if a ** b <= 64:
        return 1
    else:
        return 0

# func(4,3) と func(3,4) の戻り値をそれぞれ変数に代入
x = func(4, 3)   # 4**3 = 64 → 64 <= 64 → x = 1
y = func(3, 4)   # 3**4 = 81 → 81 > 64 → y = 0

# bool() 関数で True/False に変換して z に格納
z = [bool(x), bool(y)]

# 出力
print(z)   # → [True, False]

# --- bool() 関数について ---
# bool() は値を True / False に変換する関数
# ・0、None、""（空文字）、空のリストなどは False
# ・それ以外の数値や文字列、要素があるリストは True

