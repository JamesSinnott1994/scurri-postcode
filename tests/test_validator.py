import unittest
from postcode.validator import Validator

class TestPostcodeFormatter(unittest.TestCase):
    def test_postcode_length_validity(self):
        self.assertEqual(Validator.validate("CR2"), False)
        self.assertEqual(Validator.validate("CR2 6XH"), True)
        self.assertEqual(Validator.validate("CR2 6XHHI"), False)

    def test_postcode_format_validity(self):
        self.assertEqual(Validator.validate("AA9 9AA"), True)
        self.assertEqual(Validator.validate("AA 9AA"), False)
        self.assertEqual(Validator.validate("AA9A 9AA"), True)
        self.assertEqual(Validator.validate("AA 9AA"), False)
        self.assertEqual(Validator.validate("99 9AA"), False)

    def test_postcode_letter_validity(self):
        # First position check
        result = Validator.postcode_letter_checker("Q1A OAX", "A9A 9AA")
        self.assertFalse(result)
        result = Validator.postcode_letter_checker("W1A OAX", "A9A 9AA")
        self.assertTrue(result)

        # Second position check
        result = Validator.postcode_letter_checker("DI55 1PT", "AA99 9AA")
        self.assertFalse(result)
        result = Validator.postcode_letter_checker("DN55 1PT", "AA99 9AA")
        self.assertTrue(result)

        # Third position check
        result = Validator.postcode_letter_checker("W1Z 0AX", "A9A 9AA")
        self.assertFalse(result)
        result = Validator.postcode_letter_checker("W1A 0AX", "A9A 9AA")
        self.assertTrue(result)

        # Fourth position check
        result = Validator.postcode_letter_checker("EC1I 1BB", "AA9A 9AA")
        self.assertFalse(result)
        result = Validator.postcode_letter_checker("EC1A 1BB", "AA9A 9AA")
        self.assertTrue(result)

        # Final two letters check
        result = Validator.postcode_letter_checker("EC1I 1CB", "AA9A 9AA")
        self.assertFalse(result)
        result = Validator.postcode_letter_checker("EC1I 1BI", "AA9A 9AA")
        self.assertFalse(result)
        result = Validator.postcode_letter_checker("EC1I 1OV", "AA9A 9AA")
        self.assertFalse(result)
        result = Validator.postcode_letter_checker("EC1A 1BB", "AA9A 9AA")
        self.assertTrue(result)
    
    def test_postcode_details_output(self):
        postcode = "DN55 1PT"
        self.assertEqual(
            Validator.retrieve_details(postcode), 
            "Postcode details: {'area': 'DN', 'district': '55', 'sector': '1', 'unit': 'PT'}\n")
    
if __name__ == "__main__":
    unittest.main()