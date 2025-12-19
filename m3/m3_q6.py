def adjust_recipe(recipe_kosaji, recipe_servs, cook_servs):
    adjust_kosaji = recipe_kosaji * cook_servs / recipe_servs  # (30)
    return adjust_kosaji


def round_kosaji(adjust_kosaji):
    int_part = int(adjust_kosaji)
    frac_part = adjust_kosaji - int_part  # (31)
    if frac_part >= 0.5:
        return str(int_part) + '.5'
    else:
        return str(int_part)


recipe_servs = int(input('レシピは何人前？: '))

saji_type = ''
while saji_type not in ['L', 'S']:  # (32)
    saji_type = input('レシピのさじの種類は？（大さじはL、小さじはS）: ')

saji_name = '大さじ' if saji_type == 'L' else '小さじ'
recipe_saji = float(input(f'レシピは{saji_name}何杯？: '))

cook_servs = int(input('作る料理は何人前？: '))

recipe_kosaji = recipe_saji * 3 if saji_type == 'L' else recipe_saji  # (33)
adjust_kosaji = adjust_recipe(recipe_kosaji, recipe_servs, cook_servs)

cook_oosaji = adjust_kosaji // 3  # (34)

print(f'{cook_servs}人前では，大さじが{cook_oosaji:.0f}杯と'
      f'小さじが{round_kosaji(adjust_kosaji)}杯です。')

