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