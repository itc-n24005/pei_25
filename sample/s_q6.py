import random
import sys

# (英語, 日本語) のタプルを要素にもつリスト
words = [
    ('apple', 'りんご'), ('banana', 'バナナ'),
    ('coconut', 'ココナッツ'), ('doughnut', 'ドーナッツ'),
    ('effort', '努力'), ('future', '未来'),
    ('house', '家'), ('information', '情報'),
    ('gorilla', 'ゴリラ'), ('journey', '旅')
]

questions = int(input('出題数を入力: '))

length = len(words)

# 出題数が登録単語数を超えていたら終了
if length < questions:  # (30)
    print('登録された単語数以下の数値を入力してください。')
    sys.exit()

count = 0
correct = 0

while count < questions:
    # 単語をシャッフル
    random.shuffle(words)

    # 正解の選択肢番号（0〜3）
    ans_index = random.randint(0, 3)

    # 問題文（英単語）
    print(f'問題{count + 1}: {words[ans_index][0]} の意味は？')  # (31)

    # 4択を表示
    for i in range(4):  # (32)
        print(f'{i + 1}: {words[i][1]}')  # (33)

    answer = input('1から4の数字で解答（終了する場合は"x"を入力）: ')
    if answer == 'x':
        break

    print(f'あなたの解答: {answer}')

    # 正解判定
    if answer == str(ans_index + 1):  # (34)
        print('正解！')
        correct += 1
    else:
        print(f'不正解！ 正解は {ans_index + 1} の {words[ans_index][1]} でした！')

    count += 1

print(f'成績：正解{correct}問（全{count}問）')

