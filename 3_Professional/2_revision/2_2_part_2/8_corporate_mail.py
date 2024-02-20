from string import digits

MAIL_DOMAIN = '@beegeek.bzz'


existing_names = []
new_names = []

for _ in range(int(input())):
    name, _ = input().split('@')
    existing_names.append(name)

for _ in range(int(input())):
    name = input()
    name_count = 0
    while name in existing_names:
        name_count += 1
        name = name.rstrip(digits) + str(name_count)
    existing_names.append(name)
    new_names.append(name)

all_emails = list(map(lambda c: c + MAIL_DOMAIN, new_names))

print(*all_emails, sep='\n')