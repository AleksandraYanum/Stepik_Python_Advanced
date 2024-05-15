import sys


COMMENT_SIGN = '#'

for line in sys.stdin:
    if not line.strip().startswith(COMMENT_SIGN):
        sys.stdout.write(line)
