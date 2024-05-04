from pprint import pprint
import numpy as np


class Cards:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.symbols = (
            ('２ ', '３ ', '４ ', '５ ', '６ ', '７ ', '８ ', '９ ', '１０', '👨', '👸🏻', '🤴🏻', 'A '),
            ('❤', '♠', '♣', '♦'),
            ('|', '―')
        )

    def __str__(self):
        return f'|{self.symbols[0][self.rank - 2]} ― {self.symbols[1][self.suit - 1]}|'

    def __lt__(self, other):
        if self.suit == other.suit:
            return self.rank < other.rank
        else:
            return None

    def __le__(self, other):
        if self.suit == other.suit:
            return self.rank <= other.rank
        else:
            return None

    def __gt__(self, other):
        if self.suit == other.suit:
            return self.rank > other.rank
        else:
            return None

    def __ge__(self, other):
        if self.suit == other.suit:
            return self.rank >= other.rank
        else:
            return None


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

    def start_game(self):
        dealed = self.deal_cards()
        end_game = False
        cards_on_desk = [[], []]
        while not end_game:
            print('First player\n     0         1         2         3         4         5     ')
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
            print('\n     0         1         2         3         4         5     \nSecond player')
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


GameFool(6, 2).start_game()