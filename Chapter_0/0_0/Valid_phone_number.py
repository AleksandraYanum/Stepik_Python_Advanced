PATTERN_DIGIT_CHAR = 'd'
PATTERN_SEP_CHAR = 'p'

PATTERN_SEP_LIST = '-_.,:'


def check_phone_number(phone_number, pattern_list):
    is_any_pattern_matched = False

    phone_number_len = len(phone_number)

    for pattern in pattern_list:
        is_pattern_matched = True

        if phone_number_len != len(pattern):
            is_pattern_matched = False
        else:
            for i in range(phone_number_len):

                if pattern[i] == PATTERN_DIGIT_CHAR:
                    if not phone_number[i].isdigit():
                        is_pattern_matched = False
                        break

                elif pattern[i] == PATTERN_SEP_CHAR:
                    if phone_number[i] not in PATTERN_SEP_LIST:
                        is_pattern_matched = False
                        break

                elif pattern[i] != phone_number[i]:
                    is_pattern_matched = False
                    break

        if is_pattern_matched:
            is_any_pattern_matched = True
            break

    return is_any_pattern_matched


##################################################################################

PATTERN_LIST = ['7-ddd-ddd-dddd', '7-dddpddpdd', 'ddd-ddd-dddd', '+375-dd-ddd-dddd', 'X_1_dps']
VALID_MSG = "Phone number is VALID"
NOT_VALID_MSG = "Phone number is NOT VALID"


def main():
    phone_number = input()

    is_phone_valid = check_phone_number(phone_number, PATTERN_LIST)

    output = NOT_VALID_MSG
    if is_phone_valid:
        output = VALID_MSG

    print(output)


main()
