input_text = input().upper()

phone_digits = [str(num) for num in range(10)]
digit_chars = [" ", ".,?!:", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
phone_digit_chars = dict(zip(phone_digits, digit_chars))

output_digits = []

for c in input_text:
    for key, value in phone_digit_chars.items():
        if c in value:
            output_digits.append(key * (value.index(c) + 1))
            break

print(*output_digits, sep='')