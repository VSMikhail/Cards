from Cards import Cards
import numpy as np
import random


def move_cards(move_from, indexes, move_to):
    [move_to.append(move_from.pop(index)) for index in sorted(indexes, reverse=True)]


class GameFool:
    def __init__(self, deck_start, players_number):
        self.deck_start = deck_start
        self.players_number = players_number
        self.deck = [Cards(rank, suit) for rank in range(self.deck_start, 15) for suit in range(1, 5)]
        self.cards_in_hands = [[] for _ in range(0, self.players_number)]
        self.beaten_cards = []

    def add_cards_to_hands(self):
        for _ in self.cards_in_hands:
            move_cards(self.deck, range(0, len(_) - 6, -1), _)

    def deal_cards(self):
        random.shuffle(self.deck)
        self.add_cards_to_hands()
        print(f'|X----------X|\n|X    XX    X|\n|X__________X|\n  {self.deck[0]}')

    def play_round(self, who_goes, who_beat):
        end_round = False
        cards_on_desk = [[], []]
        while not end_round:
            print('First player\n' + '    '.join(['     ' + str(_) for _ in range(0, len(self.cards_in_hands[who_goes]))]))
            for _ in self.cards_in_hands[who_goes]:
                print(_, end='')
            print('\n\n')
            for _ in cards_on_desk[0]:
                print(_, end='')
            print('')
            for _ in cards_on_desk[1]:
                print(_, end='')
            print('\n\n')
            for _ in self.cards_in_hands[who_beat]:
                print(_, end='')
            print('\n' + '    '.join(['     ' + str(_) for _ in range(0, len(self.cards_in_hands[who_beat]))]) + '\nSecond player')
            first_choice = int(input('First player goes: '))
            if first_choice == 100:
                print('All beaten!')
                move_cards(cards_on_desk[0], range(0, len(cards_on_desk[0])), self.beaten_cards)
                move_cards(cards_on_desk[1], range(0, len(cards_on_desk[1])), self.beaten_cards)
                break
            first_player_card = self.cards_in_hands[who_goes][first_choice]
            move_cards(self.cards_in_hands[who_goes], [first_choice], cards_on_desk[0])
            if first_player_card in cards_on_desk[0] or first_player_card in cards_on_desk[1] or not cards_on_desk[0]:
                second_choice = int(input('Second player goes: '))
                if second_choice == 100:
                    print('Take all!')
                    move_cards(cards_on_desk[0], range(0, len(cards_on_desk[0])), self.cards_in_hands[who_beat])
                    move_cards(cards_on_desk[1], range(0, len(cards_on_desk[1])), self.cards_in_hands[who_beat])
                    break
                second_player_card = self.cards_in_hands[who_beat][second_choice]
                if second_player_card > first_player_card:
                    print('Second card win')
                    move_cards(self.cards_in_hands[who_beat], [second_choice], cards_on_desk[1])
                elif second_player_card < first_player_card:
                    print('First card win')
                else:
                    print('Wrong suit')
            else:
                print('Wrong card')