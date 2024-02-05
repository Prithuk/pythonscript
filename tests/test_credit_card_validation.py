

import unittest
from datetime import date
from src.credit_card_validation import validateCard



class CreditCardValidationTest(unittest.TestCase):
    def test_validateCard_valid(self):
        self.assertEqual(validateCard(date(2025, 2, 10)), 'Valid')
    
    def test_validateCard_invalid(self):
        with self.assertRaises(RuntimeError):
            validateCard(date(2022, 2, 10))

# if __name__ == '__main__':
#     unittest.main()
