from pprint import pprint
from Game import GameFool


game = GameFool(6, 2)
game.deal_cards()
game.play_round(0, 1)
print('\nКарты первого')
for _ in game.cards_in_hands[0]:
    print(_)
print('\nКарты второго')
for _ in game.cards_in_hands[1]:
    print(_)
print('\nБито')
for _ in game.beaten_cards:
    print(_)
