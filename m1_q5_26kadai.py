# 変数 a に 2 を代入
a = 2

# 空のリストを用意
nums = []

# 6回繰り返してリストに値を追加する
for i in range(6):
    nums.append(a)  # numsリストの末尾に現在のaの値を追加する
    a = a * 2       # a を倍に更新する

# 完成したリストを表示
print(nums)

