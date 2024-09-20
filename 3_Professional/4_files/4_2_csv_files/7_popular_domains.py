from csv import DictReader, DictWriter
from collections import defaultdict


DOMAIN_SYM = '@'
EMAIL_COL_NAME = 'email'
DOMAIN_COL_NAME = 'domain'
DOMAIN_AMOUNT_COL_NAME = 'count'
DELIMETER_SYM = ','


def get_domain(email):
    domain = email.split(DOMAIN_SYM)[-1]
    return domain


def count_domain_usage(input_file, output_file):
    domain_count_dict = defaultdict(int)
    
    with open(input_file, encoding='utf-8') as file:
        user_data = DictReader(file)
        
        for user in user_data:
            domain = get_domain(user[EMAIL_COL_NAME])
            domain_count_dict[domain] += 1 
    
    # Sort by amount and alphabet
    sorted_domains = sorted(domain_count_dict.items(), key=lambda x: (x[1], x[0]))
    
    with open(output_file, 'w', encoding='utf-8', newline='') as file:
        headers = [DOMAIN_COL_NAME, DOMAIN_AMOUNT_COL_NAME]
        domain_data = DictWriter(file, fieldnames=headers)
        domain_data.writeheader()

        for domain, count in sorted_domains:
            domain_data.writerow({DOMAIN_COL_NAME: domain, DOMAIN_AMOUNT_COL_NAME: count})

        
def main():
    count_domain_usage('data.csv', 'domain_usage.csv')
    

main()





