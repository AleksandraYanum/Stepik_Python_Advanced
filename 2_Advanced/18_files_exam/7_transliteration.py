CYRYLLIC_TO_LATIN_DICT = \
{
    'а': 'a', 
    'к': 'k', 
    'х': 'h', 
    'б': 'b', 
    'л': 'l', 
    'ц': 'c', 
    'в': 'v', 
    'м': 'm', 
    'ч': 'ch',
    'г': 'g', 
    'н': 'n', 
    'ш': 'sh', 
    'д': 'd', 
    'о': 'o', 
    'щ': 'shh', 
    'е': 'e', 
    'п': 'p', 
    'ъ': '*',
    'ё': 'jo', 
    'р': 'r', 
    'ы': 'y', 
    'ж': 'zh', 
    'с': 's', 
    'ь': "'", 
    'з': 'z', 
    'т': 't', 
    'э': 'je',
    'и': 'i', 
    'у': 'u', 
    'ю': 'ju', 
    'й': 'j', 
    'ф': 'f', 
    'я': 'ya'
    }


with open('cyrillic.txt', encoding='utf-8') as cyrillic_input, \
open('transliteration.txt',  'w', encoding='utf-8') as latin_output:

        for line in cyrillic_input:
                for char in line:
                        lower_char = char.lower()
                        trans_lower_char = CYRYLLIC_TO_LATIN_DICT.get(lower_char, char)
                        trans_char = trans_lower_char.capitalize() if char.isupper() else trans_lower_char
                        
                        latin_output.write(trans_char)