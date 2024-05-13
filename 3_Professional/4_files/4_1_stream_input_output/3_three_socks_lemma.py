import sys
from itertools import cycle


PLAYERS = cycle(['Анри', 'Дима'])


last_turn_socks_amount = 0


for line in sys.stdin:
    socks_amount = int(line.strip())
    last_turn_socks_amount = socks_amount
    сurrent_player = next(PLAYERS)

winner = сurrent_player if last_turn_socks_amount % 2 == 0 else next(PLAYERS)

print(winner)