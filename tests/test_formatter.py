import unittest
from postcode.formatter import Formatter

class TestPostcodeFormatter(unittest.TestCase):
    def test_formatter_output(self):
        self.assertEqual(Formatter.format("cr26xh"), "CR2 6XH")
        self.assertEqual(Formatter.format("dn551pt"), "DN55 1PT")
        self.assertEqual(Formatter.format("m11aE"), "M1 1AE")
        self.assertEqual(Formatter.format("   M1 1AE    "), "M1 1AE")

    def test_postcode_converter_output(self):
        self.assertEqual(Formatter.convert_postcode("CR2 6XH"), "AA9 9AA")
        self.assertEqual(Formatter.convert_postcode("DN55 1PT"), "AA99 9AA")
        self.assertEqual(Formatter.convert_postcode("M1 1AE"), "A9 9AA")
        self.assertEqual(Formatter.convert_postcode("B33 8TH"), "A99 9AA")
        self.assertEqual(Formatter.convert_postcode("W1A 0AX"), "A9A 9AA")
        self.assertEqual(Formatter.convert_postcode("EC1A 1BB"), "AA9A 9AA")

    def test_get_postcode_with_space(self):
        self.assertEqual(Formatter.get_postcode_with_space("CR26XH"), "CR2 6XH")
        self.assertEqual(Formatter.get_postcode_with_space("DN551PT"), "DN55 1PT")
        self.assertEqual(Formatter.get_postcode_with_space("M1 1AE"), "M1 1AE")

    def test_get_postcode_area(self):
        self.assertEqual(Formatter.get_postcode_area("DN55"), "DN")
        self.assertEqual(Formatter.get_postcode_area("M1"), "M")

    def test_get_postcode_district(self):
        self.assertEqual(Formatter.get_postcode_district("CR2"), "2")
        self.assertEqual(Formatter.get_postcode_district("DN55"), "55")
        self.assertEqual(Formatter.get_postcode_district("W1A"), "1A")
        self.assertEqual(Formatter.get_postcode_district("EC1A"), "1A")

    def test_get_postcode_sector(self):
        self.assertEqual(Formatter.get_postcode_sector("6XH"), "6")
        self.assertEqual(Formatter.get_postcode_sector("1PT"), "1")

    def test_get_postcode_unit(self):
        self.assertEqual(Formatter.get_postcode_unit("6XH"), "XH")
        self.assertEqual(Formatter.get_postcode_unit("1PT"), "PT")
    
if __name__ == "__main__":
    unittest.main()