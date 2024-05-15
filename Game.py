from Cards import Cards
import random


def move_cards(move_from, indexes, move_to):
    [move_to.append(move_from.pop(index)) for index in sorted(indexes, reverse=True)]


class GameFool:
    def __init__(self, deck_start, players_number):
        self.deck_start = deck_start
        self.players_number = players_number
        self.deck = [Cards(rank, suit, 0) for rank in range(self.deck_start, 15) for suit in range(1, 5)]
        self.cards_in_hands = [[] for _ in range(0, self.players_number)]
        self.beaten_cards = []
        self.cards_on_desk = [[], []]
        self.trumps = None

    def add_cards_to_hands(self):
        for _ in self.cards_in_hands:
            cards_needed = len(_) - 6
            if len(self.deck) >= 6:
                move_cards(self.deck, range(0, cards_needed, -1), _)
            elif (len(self.deck) + cards_needed) >= 0:
                move_cards(self.deck, range(0, cards_needed, -1), _)
            elif (len(self.deck) + cards_needed) < 0:
                move_cards(self.deck, range(0, - len(self.deck), -1), _)
            else:
                break

    def deal_cards(self):
        random.shuffle(self.deck)
        self.deck = [Cards(card.rank, card.suit, 1) if card.suit == self.deck[0].suit else card for card in self.deck ]
        print(f'|X----------X|\n|X    XX    X|\n|X__________X|\n  {self.deck[0]}')
        self.trumps = self.deck[0].symbols[1][self.deck[0].suit - 1]
        self.add_cards_to_hands()

    def print_desk(self):
        print(f'{self.trumps} are trumps')
        print(f'1 player\n' + '    '.join(['     ' + str(_) for _ in range(0, len(self.cards_in_hands[0]))]))
        for _ in self.cards_in_hands[0]:
            print(_, end='')
        print('\n\n')
        for _ in self.cards_on_desk[0]:
            print(_, end='')
        print('')
        for _ in self.cards_on_desk[1]:
            print(_, end='')
        print('\n\n')
        for _ in self.cards_in_hands[1]:
            print(_, end='')
        print('\n' + '    '.join(
            ['     ' + str(_) for _ in range(0, len(self.cards_in_hands[1]))]) + f'\n2 player')

    def play_round(self, who_goes, who_beat):
        continue_round = True
        while continue_round:
            self.print_desk()
            first_choice = int(input(f'{who_goes + 1} player goes: '))
            if first_choice == 100:
                print('All beaten!')
                move_cards(self.cards_on_desk[0], range(0, len(self.cards_on_desk[0])), self.beaten_cards)
                move_cards(self.cards_on_desk[1], range(0, len(self.cards_on_desk[1])), self.beaten_cards)
                break
            first_player_card = self.cards_in_hands[who_goes][first_choice]
            if first_player_card in self.cards_on_desk[0] or first_player_card in self.cards_on_desk[1] or not self.cards_on_desk[0]:
                move_cards(self.cards_in_hands[who_goes], [first_choice], self.cards_on_desk[0])
                self.print_desk()
                while True:
                    second_choice = int(input(f'{who_beat + 1} player goes: '))
                    if second_choice == 100:
                        print('Take all!')
                        while True:
                            first_choice = int(input(f'{who_goes + 1} player toss: '))
                            if first_choice == 100:
                                print('Will not')
                                break
                            first_player_card = self.cards_in_hands[who_goes][first_choice]
                            if first_player_card in self.cards_on_desk[0] or first_player_card in self.cards_on_desk[
                                1] or not self.cards_on_desk[0]:
                                move_cards(self.cards_in_hands[who_goes], [first_choice], self.cards_on_desk[0])
                                self.print_desk()

                        move_cards(self.cards_on_desk[0], range(0, len(self.cards_on_desk[0])),
                                   self.cards_in_hands[who_beat])
                        move_cards(self.cards_on_desk[1], range(0, len(self.cards_on_desk[1])),
                                   self.cards_in_hands[who_beat])
                        continue_round = False
                        break
                    second_player_card = self.cards_in_hands[who_beat][second_choice]
                    if second_player_card > first_player_card:
                        move_cards(self.cards_in_hands[who_beat], [second_choice], self.cards_on_desk[1])
                        break
                    elif second_player_card < first_player_card:
                        print('Wrong card')
                    else:
                        print('Wrong suit')
            else:
                print('Wrong card')