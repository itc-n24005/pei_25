def fukuri(ganpon, nenri, nensu):
    # 複利：毎年「残高 × 年利」分だけ増やす
    zandaka = ganpon * 10000
    for i in range(nensu):
        zandaka += zandaka * nenri   # (30)
    return int(zandaka)


def tanri(ganpon, nenri, nensu):
    # 単利：毎年「元本 × 年利」分だけ増やす
    zandaka = ganpon * 10000
    for i in range(nensu):
        zandaka += ganpon * 10000 * nenri   # (31)
    return int(zandaka)


def hikaku(ganpon, nenri, nensu):
    print(f'元本{ganpon}万円，年利{nenri:.0%}で{nensu}年間預けた場合')
    fu = fukuri(ganpon, nenri, nensu) / 10000
    ta = tanri(ganpon, nenri, nensu) / 10000
    # 複利 - 単利 を小数1桁で表示
    print(f'複利の方が{fu - ta:.1f}万円多く受け取ることができます')  # (32)


def hitsuyou_nensu(ganpon, nenri, uketori):
    print(f'年利{nenri:.0%}で利子を{uketori}万円受け取るには')

    # 複利の必要年数
    kaku_f = 0
    year_f = 0
    while kaku_f < uketori * 10000:   # (33)
        kaku_f = fukuri(ganpon, nenri, year_f + 1) - ganpon * 10000
        year_f += 1

    # 単利の必要年数
    kaku_t = 0
    year_t = 0
    while kaku_t < uketori * 10000:   # (33)
        kaku_t = tanri(ganpon, nenri, year_t + 1) - ganpon * 10000  # (34)
        year_t += 1

    print(f'複利で{year_f}年、単利で{year_t}年かかります')


# 実行例
hikaku(100, 0.05, 10)
hitsuyou_nensu(100, 0.05, 300)

