import unittest
from shop import check_affordability, check_extra_money, InsufficientFundsError

class ShopTests(unittest.TestCase):

    def test_check_affordability(self):
        prices = {"Wardrobe": 75, "Rug": 20, "Art": 1000}
        balance = 50
        purchase_attempts = 2
        user_input = "Art"
        check_affordability(user_input, prices, balance, purchase_attempts)

    def test_check_extra_money(self):
        prices = {"Wardrobe": 75, "Rug": 20, "Art": 1000}
        user_input = "Art"
        more_money = 900
        with self.assertRaises(InsufficientFundsError) as cm:
            check_extra_money(more_money, user_input, prices)
        self.assertEqual(str(cm.exception), "Insufficient funds even with extra money")


if __name__ == '__main__':
    unittest.main()

# Marks (9/14) -- Atleast 5 unit tests should be written to cover valid, invalid and boundary cases
