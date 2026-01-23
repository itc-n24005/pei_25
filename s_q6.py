import random  # shuffle(), randint() を使うため
import sys     # sys.exit() で終了するため

# 英単語と日本語の意味をタプルで管理する（(英語, 日本語)）
words = [
    ('apple', 'りんご'),
    ('banana', 'ばなな'),
    ('coconut', 'ココナッツ'),
    ('donut', 'ドーナツ'),
    ('effort', '努力'),
    ('future', '未来'),
    ('gorilla', 'ゴリラ'),
    ('house', '家'),
    ('information', '情報'),
    ('journey', '旅')
]

# 出題数を受け取る
questions = int(input('出題数を入力: '))

length = len(words)  # 登録されている単語数

# 出題数が単語数を超える場合は問題を作れないので終了する
if length < questions:
    print('登録された単語数以下の数値を入力してください')
    sys.exit()

count = 0    # 何問出題したか
correct = 0  # 何問正解したか

while count < questions:
    # 毎回シャッフルして、先頭4つを選択肢として使う
    random.shuffle(words)

    # 4択の中から正解の位置(0〜3)をランダムに決める
    ans_index = random.randint(0, 3)

    # 問題文（英単語）を表示
    print(f'\n問題{count + 1}: {words[ans_index][0]} の意味は？')

    # 重要：選択肢は必ず 1〜4 を全部表示する（表示と判定のズレ防止）
    for i in range(4):
        print(f'{i + 1}: {words[i][1]}')

    # 解答入力（xなら途中終了）
    answer = input('1から4の数字で解答(終了するには"x"を入力): ')
    if answer == 'x':
        break

    print(f'あなたの解答: {answer}')

    # input()は文字列なので、正解番号(ans_index+1)も文字列にして比較する
    if answer == str(ans_index + 1):
        print('正解！')
        correct += 1
    else:
        print(f'不正解！正解は {ans_index + 1} の「{words[ans_index][1]}」でした！')

    count += 1

# 最終成績（途中終了した場合 count が実際に解いた数になる）
print(f'\n成績: 正解{correct}問 (全{count}問)')

