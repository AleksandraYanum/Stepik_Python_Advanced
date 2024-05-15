HIDING_SYM = '*'
ALL_DIGIT_AMOUNT = 16
NOT_HIDED_DIGIT_AMOUNT = 4
HIDING_SYM_AMOUNT = ALL_DIGIT_AMOUNT - NOT_HIDED_DIGIT_AMOUNT


def hide_card(card_number):
    card_number_only_digit = card_number.replace(' ', '')
    hided_card_number = HIDING_SYM * HIDING_SYM_AMOUNT + card_number_only_digit[- NOT_HIDED_DIGIT_AMOUNT:]
    return hided_card_number