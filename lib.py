def find_all(source, symb):
    symbol_idx_list = []
    start_idx = 0
    symbol_idx = source.find(symb, start_idx)

    while symbol_idx != -1:
        symbol_idx_list.append(symbol_idx)
        start_idx = symbol_idx + 1
        symbol_idx = source.find(symb, start_idx)

    return symbol_idx_list