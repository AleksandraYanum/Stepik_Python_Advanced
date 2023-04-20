PATTERN_DIGIT = 'd'
# PATTERN_SEP = '-'


def check_phone_number(phone_number, pattern):
    is_pattern_matched = True
    phone_number_len = len(phone_number)

    if phone_number_len != len(pattern):
        is_pattern_matched = False
    else:
        for i in range(phone_number_len):

            if pattern[i] == PATTERN_DIGIT:
                if not phone_number[i].isdigit():
                    is_pattern_matched = False
                    break

            elif pattern[i] != phone_number[i]:
                is_pattern_matched = False
                break

    return is_pattern_matched


##################################################################################

PHONE_PATTERN = '7-ddd-ddd-dddd'
VALID_MSG = "Phone number is VALID"
NOT_VALID_MSG = "Phone number is NOT VALID"


def main():
    phone_number = input()

    is_phone_valid = check_phone_number(phone_number, PHONE_PATTERN)

    output = NOT_VALID_MSG
    if is_phone_valid:
        output = VALID_MSG

    print(output)


main()
