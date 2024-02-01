# Implement test func:
# 1. Read input file with test data from Stepik
# 2. Merge #1 with file to test and save to new file
# 3. Execute #2 file and save output to result file
# 4. Compare #3 with the expected output file and write comparison results


HIDING_SYM = '*'
ALL_DIGIT_AMOUNT = 16
NOT_HIDED_DIGIT_AMOUNT = 4
HIDING_SYM_AMOUNT = ALL_DIGIT_AMOUNT - NOT_HIDED_DIGIT_AMOUNT


def hide_card(card_number):
    card_number_only_digit = card_number.replace(' ', '')
    hided_card_number = HIDING_SYM * HIDING_SYM_AMOUNT + card_number_only_digit[- NOT_HIDED_DIGIT_AMOUNT:]
    return hided_card_number

