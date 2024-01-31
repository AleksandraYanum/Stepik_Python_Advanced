# Code is loger, but with 1 loop
def convert(string):
    lower_alpha_count = 0
    upper_alpha_count = 0
    
    for sym in string:
        if sym.isalpha():
            if sym.islower():
                lower_alpha_count += 1
            else:
                upper_alpha_count += 1
      
    edited_string = string.lower() if lower_alpha_count >= upper_alpha_count else string.upper()

    return edited_string

# Shorter, but with 2 loops
def convert_v2(string):
    edited_string = string.lower() if sum(map(str.islower, string)) >= sum(map(str.isupper, string)) else string.upper() 

    return edited_string

# Short and with 1 loop, but complicated
def convert_v3(string):
    edited_string = string.lower() if sum(map(lambda c: (1 if c.isupper() else -1) if c.isalpha() else 0, string)) <= 0 else string.upper()
    
    return edited_string


def main():
    print(convert('pi31415!'))


main()