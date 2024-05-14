from pprint import pprint
from Game import GameFool
from Cards import Cards


game = GameFool(6, 2)
game.deal_cards()
end_game = True
beat, goes = 0, 1
while end_game:
    start_beaten_cards = len(game.beaten_cards)
    game.play_round(beat, goes)
    if len(game.beaten_cards) > start_beaten_cards:
        beat, goes = goes, beat
    game.add_cards_to_hands()

print('\nКарты первого')
for _ in game.cards_in_hands[0]:
    print(_)
print('\nКарты второго')
for _ in game.cards_in_hands[1]:
    print(_)
print('\nБито')
for _ in game.beaten_cards:
    print(_)
