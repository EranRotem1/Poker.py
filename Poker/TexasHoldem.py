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

    def __str__(self):
        return f"{self.rank} of {self.suit}"

print(Card("2", "Hearts"))
print(Card("Ace", "Spades"))

