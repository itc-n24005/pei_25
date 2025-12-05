def check_num(num):
    a = num[1]
    b = num[-1]
    c = len(num) == 919
    d = len(num) > 0

    # ★ ここで a,b,c,d の type を出力 ★
    print(f"変数aのtypeは{type(a)}")
    print(f"変数bのtypeは{type(b)}")
    print(f"変数cのtypeは{type(c)}")
    print(f"変数dのtypeは{type(d)}")

    # ★ m3_q4_20 と同じ条件分岐部分 ★
    if a == b and c and d:
        print(a * b)
    elif a == b or c or d:
        print(b * 2)

num = '919'
check_num(num)

