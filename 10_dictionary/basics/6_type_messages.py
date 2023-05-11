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


input_text = input().upper()

output_digits = []

for c in input_text:
    for key, value in PHONE_DIGIT_CARS.items():
        if c in value:
            output_digits.append(key * (value.index(c) + 1))
            break

print(*output_digits, sep='')