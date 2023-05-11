PHONE_DIGIT_CHARS = {
    "0": " ",
    "1": ".,?!:",
    "2": "ABC",
    "3": "DEF",
    "4": "GHI",
    "5": "JKL",
    "6": "MNO",
    "7": "PQRS",
    "8": "TUV",
    "9": "WXYZ",
}


phone_char_digits = {}
for digit, chars in PHONE_DIGIT_CHARS.items():
    for i in range(len(chars)):
        phone_char_digits[chars[i]] = digit * (i + 1)

input_text = input().upper()

output_digits = []

for c in input_text:
    if c in phone_char_digits:
        output_digits.append(phone_char_digits[c])

print(*output_digits, sep='')