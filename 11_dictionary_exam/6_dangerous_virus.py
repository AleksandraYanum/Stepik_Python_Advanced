ACTION_CODES =  {'write': 'W', 
                 'read': 'R',
                 'execute': 'X'}

PERMISSON_OUTPUT = 'OK'
PROHIBITION_OUTPUT = 'Access denied'


file_permissons = {}

for _i in range(int(input())):
    file, *permissions = input().split()
    file_permissons[file] = set(permissions)

permission_result_list = []

for _ in range(int(input())):
    action, file = input().split()
    is_permitted = ACTION_CODES[action] in file_permissons[file]
    permission_result_list.append(is_permitted)


for permission_result in permission_result_list:
    output_result = PERMISSON_OUTPUT if permission_result else PROHIBITION_OUTPUT
    print(output_result)
