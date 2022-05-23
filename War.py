import random
from time import sleep
import pdb

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit

    def value(self):
        return values[self.rank]


class Deck:
    def __init__(self):
        self.deck = []

        for rank in ranks:
            for suit in suits:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''  # start with an empty string
        for card in self.deck:
            deck_comp += '\n ' + card.__str__()  # add each Card object's print string
        return 'The deck has:'

    def shuffle(self):
        random.shuffle(self.deck)

    def pop(self):
        return self.deck.pop()


class Hand:
    def __init__(self):
        self.cards = []

    def tap(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)

    def extend_cards(self, cards):
        self.cards.extend(cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def how_many(self):
        return len(self.cards)


while True:
    game_deck = Deck()
    player_one = Hand()
    player_one_stack = []
    player_two = Hand()
    player_two_stack = []
    war = []
    var_1 = 26
    var_2 = 26
    rounds = 0

    print('War game AI vs AI')
    input('Press anything to continue: ')

    game_deck.shuffle()
    print('Shuffled Deck...')
    sleep(1)
    while var_1 > 0:
        player_one.add_card(game_deck.pop())
        var_1 -= 1
    while var_2 > 0:
        player_two.add_card(game_deck.pop())
        var_2 -= 1
    print('Giving cards to players...')
    sleep(1)
    while True:
        try:
            p1 = player_one.tap()
            p2 = player_two.tap()
            while p1.value() == p2.value():
                print('The war begins')
                sleep(0.2)
                war.append(p1)
                war.append(p2)
                p1 = player_one.tap()
                p2 = player_two.tap()
                war.append(p1)
                war.append(p2)
                p1 = player_one.tap()
                p2 = player_two.tap()
                if p1.value() > p2.value():
                    print('player one won')
                    player_two_stack.append(war)
                    player_two_stack.append(war)
                    sleep(.1)
                else:
                    print('Player two won')
                    player_one_stack.append(war)
                    player_one_stack.append(war)
                    sleep(.1)
            if p1.value() > p2.value():
                print('player one won')
                player_two_stack.append(p1)
                player_two_stack.append(p2)
                sleep(.1)
            else:
                print('Player two won')
                player_one_stack.append(p1)
                player_one_stack.append(p2)
                sleep(.1)

        except:
            rounds += 1
            print('The game took:')
            print(rounds)
            player_one.extend_cards(player_one_stack)
            player_one_stack = []
            player_one.shuffle()
            print('Adding cards to player one hand and shuffling it')
            player_two.extend_cards(player_two_stack)
            player_two_stack = []
            player_two.shuffle()
            print('Adding cards to player two hand and shuffling it')
            print('---------------------')
            sleep(0.1)
            if player_one.how_many() == 0:
                print('player one won the game')
                break
            elif player_two.how_many() == 0:
                print('player two won')
                break
            continue


