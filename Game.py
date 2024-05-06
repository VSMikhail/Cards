from Cards import Cards
import numpy as np

def move_cards(move_from, indexes, move_to):
    [move_to.append(move_from.pop(index)) for index in sorted(indexes, reverse=True)]


class GameFool:
    def __init__(self, deck_start, players_number):
        self.deck_start = deck_start
        self.players_number = players_number

    def create_deck(self):
        return [Cards(rank, suit) for rank in range(self.deck_start, 15) for suit in range(1, 5)]

    def deal_cards(self):
        deck = self.create_deck()
        cards_in_hands = []
        beaten_cards = []

        for _ in range(1, self.players_number + 1):
            cards_in_hand = []
            move_cards(deck, np.random.randint(0, len(deck)-1, 6), cards_in_hand)
            cards_in_hands.append(cards_in_hand)
        return deck, cards_in_hands, beaten_cards

    def print_desk(self):
        pass

    def play_round(self):
        dealed = self.deal_cards()
        end_game = False
        cards_on_desk = [[], []]
        while not end_game:
            print('First player\n' + '    '.join(['     ' + str(_) for _ in range(0, len(dealed[1][0]))]))
            for _ in dealed[1][0]:
                print(_, end='')
            print('\n\n')
            for _ in cards_on_desk[0]:
                print(_, end='')
            print('')
            for _ in cards_on_desk[1]:
                print(_, end='')
            print('\n\n')
            for _ in dealed[1][1]:
                print(_, end='')
            print('\n' + '    '.join(['     ' + str(_) for _ in range(0, len(dealed[1][1]))]) + '\nSecond player')
            first_choice = int(input('First player goes: '))
            first_player_card = dealed[1][0][first_choice]
            second_choice = int(input('Second player goes: '))
            second_player_card = dealed[1][1][second_choice]
            if second_player_card > first_player_card:
                print('Second card win')
                move_cards(dealed[1][0], [first_choice], cards_on_desk[0])
                move_cards(dealed[1][1], [second_choice], cards_on_desk[1])
            elif second_player_card < first_player_card:
                print('First card win')
            else:
                print('Wrong suit')