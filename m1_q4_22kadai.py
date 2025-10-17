a = 17
b = 5
dm = divmod(a, b)       # (商, 余り) = (3, 2)
p = pow(dm[0], dm[1])   # 3 ** 2 = 9
all_num = [a, b, dm[0], dm[1], p]
min_all = min(all_num)
max_all = max(all_num)
sum_all = sum(all_num)

# まずリストの中身を出力
print(all_num)

# min, max, sum を出力
print(f'{min_all}, {max_all}, {sum_all}')

