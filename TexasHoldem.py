# POKER
class Card():
    RANKS = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace")
    SUITS = ("Hearts", "Spades", "Diamonds", "Clubs")
    def __init__(self, rank, suit):
        if rank not in self.RANKS:
            raise ValueError(f"rank must be: {self.RANKS}")
        if suit not in self.SUITS:
            raise ValueError(f"suit must be: {self.SUITS}")
        self.rank = rank
        self.suit = suit
    
    @classmethod
    def make_52_card_deck(cls):
        return [
            cls(rank, suit)
            for rank in cls.RANKS 
            for suit in cls.SUITS
        ]

    def __repr__(self):
        return f"{self.rank} of {self.suit}"

    # def __repr__(self):
    #     return f"Card({self.rank},{self.suit})"

#test
# print(Card("2", "Hearts"))
# print(Card("Ace", "Spades"))

class Deck():
    def __init__(self):
        self.cards = []

    def __str__(self):
        return f"{self.cards}"

    def add_cards(self, cards):
        self.cards.extend(cards)
#test
# standard_deck = Card.make_52_card_deck()
# deck = Deck()
# deck.add_cards(standard_deck)
# print(deck)

class Hand():
    def __init__(self, cards):
        self.cards = cards
        if len(cards) > 2:
            raise ValueError("You can only have 2 cards")

    def __repr__(self):
        return f"{self.cards}"

#test 
# cards = [Card("Ace", "Spades"), Card("4", "Diamonds")]
# cards = [Card("Ace", "Spades"), Card("4", "Diamonds"), Card("2", "Hearts")]
# print(Hand(cards))

