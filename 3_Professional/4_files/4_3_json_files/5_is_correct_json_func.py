from json import loads, JSONDecodeError


def is_correct_json(line):
    try:
        loads(line)
        return True
    except JSONDecodeError:
        return False