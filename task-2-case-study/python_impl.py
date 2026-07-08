import unittest

def bank_transfer(balance1, balance2, amount):
    """
    Transfers money from account 1 to account 2.
    """
    if balance1 >= amount:
        balance1 -= amount
        balance2 += amount
    return balance1, balance2

class TestBankTransfer(unittest.TestCase):
    def test_normal_transfer(self):
        b1, b2 = bank_transfer(100, 50, 30)
        self.assertEqual(b1, 70)
        self.assertEqual(b2, 80)
        
    def test_insufficient_funds(self):
        b1, b2 = bank_transfer(100, 50, 150)
        self.assertEqual(b1, 100) # Transfer fails safely
        self.assertEqual(b2, 50)
        
    def test_total_money_preserved_bug(self):
        # A test suite might miss asserting that a negative amount isn't allowed.
        # If someone transfers a negative amount, meaning amount < 0,
        # balance1 >= amount will be true!
        # e.g. 100 >= -500 is True
        # balance1 becomes 100 - (-500) = 600
        # balance2 becomes 50 + (-500) = -450
        # The exact bug: Negative amounts are treated as valid transfers.
        b1, b2 = bank_transfer(100, 50, -500)
        
        # This assert proves the bug exists: money was magically created for account 1
        self.assertEqual(b1, 600)
        # And account 2 goes into unauthorized debt
        self.assertEqual(b2, -450)

if __name__ == '__main__':
    unittest.main()
