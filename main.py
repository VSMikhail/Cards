from Game import GameFool


game = GameFool(6, 2)
game.deal_cards()
continue_game = True
goes, beat = 0, 1
while continue_game:
    start_beaten_cards = len(game.beaten_cards)
    game.play_round(goes, beat)
    if len(game.beaten_cards) > start_beaten_cards:
        beat, goes = goes, beat
    game.add_cards_to_hands()
    if not game.cards_in_hands[goes]:
        print(f'{goes + 1} player win!')
        continue_game = False