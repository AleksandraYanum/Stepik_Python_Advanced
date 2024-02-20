# from string import digits

# MAIL_DOMAIN = '@beegeek.bzz'


# existing_names = []
# new_names = []

# for _ in range(int(input())):
#     name, _ = input().split('@')
#     existing_names.append(name)

# for _ in range(int(input())):
#     name = input()
#     name_count = 0
#     while name in existing_names:
#         name_count += 1
#         name = name.rstrip(digits) + str(name_count)
#     existing_names.append(name)
#     new_names.append(name)

# all_emails = list(map(lambda c: c + MAIL_DOMAIN, new_names))

# print(*all_emails, sep='\n')


from collections import defaultdict


MAIL_DOMAIN = '@beegeek.bzz'
START_IDX = -1


existing_mail_dict = defaultdict(list)
new_mails = []

for _ in range(int(input())):
    mail_head, _ = input().split('@')
    idx = START_IDX
    while mail_head[idx].isdigit():
        idx -= 1
    name = mail_head[:idx + 1] if idx != START_IDX else mail_head
    num = int(mail_head[idx + 1:]) if name != mail_head else 0
    existing_mail_dict[name].append(num)

for _ in range(int(input())):
    name = input()
    existing_name_num_list = existing_mail_dict.get(name)
    num = 0
    if existing_name_num_list:
        while num in existing_name_num_list:
            num += 1
        num_to_add = num

    num_to_add = num if num else ''

    existing_mail_dict[name].append(num)
    new_mails.append(name + str(num_to_add) + MAIL_DOMAIN)

print(*new_mails, sep='\n')

        





