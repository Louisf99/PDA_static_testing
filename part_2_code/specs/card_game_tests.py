import unittest
from src.card import Card
from src.card_game import *

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.seven_of_diamonds = Card("diamond", 7)
        self.ace_of_spades = Card("ace", 1)
        self.ten_of_clubs = Card("club", 10)
        self.six_of_spades = Card("spade", 6)
        self.five_of_hearts = Card("heart", 5)

    def test_card_has_value(self):
        self.assertEqual(7, self.seven_of_diamonds.value)

    def test_card_has_suite(self):
        self.assertEqual("diamond", self.seven_of_diamonds.suit)

    def test_check_for_ace_True(self):
        ace = check_for_ace(self.ace_of_spades)
        self.assertEqual(True, ace)

    def test_check_for_ace_false(self):
        ace_status = check_for_ace(self.six_of_spades)
        self.assertEqual(False, ace_status)

    def test_highest_card_card1(self):
        card1_high = highest_card(self.six_of_spades, self.ace_of_spades)
        self.assertEqual(self.six_of_spades, card1_high)

    def test_highest_card_card2(self):
        card2_high = highest_card(self.seven_of_diamonds, self.ten_of_clubs)
        self.assertEqual(self.ten_of_clubs, card2_high)

    def test_cards_total(self):
        cards = [self.six_of_spades, self.ten_of_clubs, self.five_of_hearts]
        total = cards_total(cards)
        self.assertEqual("You have a total of 21", total)
