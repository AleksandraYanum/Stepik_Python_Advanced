input_text = input().upper()

phone_digits = [str(num) for num in range(10)]
digit_chars = [" ", ".,?!:", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
phone_digit_chars = dict(zip(phone_digits, digit_chars))

output_digits = []

for c in input_text:
    for key in phone_digit_chars.keys():
        if c in phone_digit_chars[key]:
            output_digits.append(key * (phone_digit_chars[key].index(c) + 1))
            break

print(*output_digits, sep='')