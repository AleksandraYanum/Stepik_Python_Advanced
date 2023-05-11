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


phone_digit_dict = {}
for digit, chars in PHONE_DIGIT_CHARS.items():
    for char in chars:
        phone_digit_dict[char] = digit * (chars.index(char) + 1)

input_text = input().upper()

output_digits = []

for c in input_text:
    if c in phone_digit_dict:
        output_digits.append(phone_digit_dict[c])

print(*output_digits, sep='')