list_a = []

for x in range(1, 31):
    if x % 2 == 0:   # 偶数ならスキップ
        continue
    list_a.append(x)

print(list_a)

