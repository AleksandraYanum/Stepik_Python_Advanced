import sys


COMMENT_SIGN = '#'


comment_count = 0

for line in sys.stdin:
    if line.strip().startswith(COMMENT_SIGN):
        comment_count += 1

print(comment_count)
