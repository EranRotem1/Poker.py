import unittest
from TexasHoldem import *

class TestCard(unittest.TestCase):
    def card_val_rank_suit_test(self):
        self.assertEqual(
            Card("2", "Hearts"),
            "2 of Hearts"
        )

class TestHand(unittest.TestCase):
    def hand_val_is_cards_list_test(self):
        cards = [Card("Ace", "Spades"), Card("4", "Diamonds")]
        self.assertEqual(
            Hand(cards),
            ["Ace of Spades", "4 of Diamods"]
        )

if __name__ == "__main__":
    unittest.main()