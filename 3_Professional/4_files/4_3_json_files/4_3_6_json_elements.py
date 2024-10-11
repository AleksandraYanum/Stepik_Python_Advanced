from sys import stdin
from json import loads


input_object = stdin.read()

json_object = loads(input_object)

for key, value in json_object.items():
    if isinstance(value, list): 
        print(f"{key}: {', '.join(map(str, value))}")
    else:
        print(f"{key}: {value}")