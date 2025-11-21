# m2_q5kadai.py

# 名前のリストを用意
names = ["鈴木太郎", "田中花子"]

# 1行目：最初の名前をそのまま表示
print(names[0])

# 数字のリスト
list_a = [12, 9, 13, 3, 7, 10]

# list_b を作成して年齢を計算
list_b = []
for i in list_a:
    list_b.append(int(i / 2 + 4))

# 2行目：私は7歳です。
print(f"私は{list_b[4]}歳です。")

# 3行目：田中花子の誕生日:7月21日
month = 0
for i in list_a[-4:-2]:  # [13, 3]
    month += int(i / 2)
day = (list_a[2] + 30) // 2  # (13 + 30) // 2 = 21
print(f"{names[1]}の誕生日:{month}月{day}日")

# 4行目：花子の誕生日:4月10日
list_c = []
for i in range(0, 12, 2):
    if i % 3 == 2:
        if list_c:      # 空リストでpopしないように一応チェック
            list_c.pop()
    else:
        list_c.append(i)

# names[1] = "田中花子" の最後2文字は "花子"
print(f"{names[1][-2:]}の誕生日:{list_c[0]}月{list_c[1]}日")

# 5行目：9（list_b の最後の要素）
print(list_b[-1])

# 6行目：課題:小山田花子の誕生日:10月13日
# 「小山」＋「田中花子」から「中」を抜いて合成
name3 = "小山" + names[1][0] + names[1][2:]  # "小山" + "田" + "花子" = "小山田花子"
month2 = list_a[-1]  # 10
day2 = list_a[2]     # 13
print(f"課題:{name3}の誕生日:{month2}月{day2}日")

