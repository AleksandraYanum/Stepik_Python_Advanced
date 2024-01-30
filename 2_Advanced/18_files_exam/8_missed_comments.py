FUNC_PREFIX = 'def '
FUNC_NAME_START_IDX = len(FUNC_PREFIX)
FUNC_NAME_END_CHAR = '('
COMMENT_CHAR = '#'
ALL_FUNCS_WITH_COMMENT_OUTPUT = ['Best Programming Team']


funcs_without_comment = []

with open(input(), encoding='utf-8') as file:
        prev_line = ' '
        for line in file:
                if line.startswith(FUNC_PREFIX) and not prev_line.startswith(COMMENT_CHAR):
                        func_name_end_idx = line.find(FUNC_NAME_END_CHAR)
                        func_name = line[FUNC_NAME_START_IDX:func_name_end_idx]
                        funcs_without_comment.append(func_name)
                prev_line = line

output = funcs_without_comment if funcs_without_comment else ALL_FUNCS_WITH_COMMENT_OUTPUT
print(*output, sep='\n')