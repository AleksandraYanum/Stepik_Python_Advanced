import turtle as t


def find_all(source, symb):
    symbol_idx_list = []
    start_idx = 0
    symbol_idx = source.find(symb, start_idx)

    while symbol_idx != -1:
        symbol_idx_list.append(symbol_idx)
        start_idx = symbol_idx + 1
        symbol_idx = source.find(symb, start_idx)

    return symbol_idx_list


def shape(side, angle_count=6):
    turn_angle = 360 / angle_count
    for _ in range(angle_count):
        t.forward(side)
        t.right(turn_angle)