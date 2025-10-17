num = 12
list_s = []
s = 2

while s <= num:
    if num % s == 0:
        num //= s
        print(num)        # num の変化を出力
        if s not in list_s:
            list_s.append(s)
    else:
        s += 1

# 最後に 1 を出力する（確実に終了を表示）
if num != 1:
    print(1)

print(list_s)

