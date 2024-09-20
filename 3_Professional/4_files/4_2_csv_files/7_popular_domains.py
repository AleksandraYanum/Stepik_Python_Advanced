import csv
from collections import defaultdict


DOMAIN_SYM = '@'
EMAIL_IDX = 2


def get_domain(email):
    domain = email.split(DOMAIN_SYM)[-1]
    return domain


def count_domain_usage(input_file, output_file):
    domain_count = defaultdict(int)
    
    with open(input_file, encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader) # Skip title
        
        for row in reader:
            domain = get_domain(row[EMAIL_IDX])
            domain_count[domain] += 1 
    
    # Sort by amount and alphabet
    sorted_domains = sorted(domain_count.items(), key=lambda x: (x[1], x[0]))
    
    # Print data to file
    with open(output_file, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['domain', 'count']) 
        writer.writerows(sorted_domains)

        
def main():
    count_domain_usage('data.csv', 'domain_usage.csv')
    

main()





