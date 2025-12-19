phrase = 'PythonPrograming'

# 重複しない文字を入れるためのリスト
list_p = []

# 文字列 phrase を1文字ずつ取り出す
for p in phrase:
    # まだ list_p に入っていない文字だけを追加する
    # → すでに出てきた文字（重複）は追加されない
    if p not in list_p:
        list_p.append(p)

# 元の文字数 - 重複を除いた文字数 = 重複している文字数
print(len(phrase) - len(list_p))

# list_p に入っている文字を横に連続して表示する
# end="" を指定することで、print の改行を無くしている
for p in list_p:
    print(p, end="")

