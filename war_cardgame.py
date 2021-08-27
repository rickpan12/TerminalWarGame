import random

suite = "H D S C".split()
rank = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

allcards = []
for r in rank:
    for s in suite:
        allcards.append((s, r))


class Deck():
    def __init__(self):
        print("Creating new ordered deck!")
        self.allcards = allcards 
    def shuffle(self):
        print('SHUFFLING DECK')
        random.shuffle(self.allcards)

    def split_in_half(self):
        return (self.allcards[0 : 26], self.allcards[26:])


class Hand():
    def __init__(self, cards):
        self.cards = cards
    
    def __str__(self):
        return f"Contains {self.cards} cards"


    def add(self, added_cards):
        self.cards.extend(added_cards)

    def remove_card(self):
        return self.cards.pop()


class Player():
    
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print(f"{self.name} has placed: {drawn_card}")
        print("\n")
        return drawn_card

    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards) < 3:
            return self.hand.cards
        for x in range(3):
            war_cards.append(self.hand.remove_card())
        return war_cards           

    def still_has_cards(self):
        return len(self.hand.cards) != 0
        



deck = Deck()
deck.shuffle()
half1, half2 = deck.split_in_half()

comp = Player("computer", Hand(half1))
name = input("What is your name? ")
user = Player(name, Hand(half2))

total_rounds = 0
war_count = 0

while user.still_has_cards() == True and comp.still_has_cards() == True:
    print("New Round Beginning!")
    print("Here are the current standings:")
    print(f"{user.name} + has the count: " + str(len(user.hand.cards)))
    print(f"{comp.name} + has the count: " + str(len(comp.hand.cards)))
    print("Play a card!")
    print('\n')
    total_rounds += 1

    table_cards = []

    c_card = comp.play_card()
    p_card = user.play_card()

    table_cards.append(c_card)
    table_cards.append(p_card)

    if c_card[1] == p_card[1]:
        print("war!")
        war_count += 1
        table_cards.extend(user.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())

        if rank.index(c_card[1]) < rank.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)

    else:
        if rank.index(c_card[1]) < rank.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)


print(f"Game over, number of rounds played: {str(total_rounds)}")
print(f"A war occurred + {str(war_count)} + times")
print(f"Does the computer sill have cards?")
print(str(comp.still_has_cards()))
print(f"Does the player sill have cards?")
print(str(user.still_has_cards()))








