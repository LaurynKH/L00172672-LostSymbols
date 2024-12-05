import unittest
from lostSymbol import Symbol

class TestSymbol(unittest.TestCase):

    def setUp(self):
        """This method will run before each test"""
        self.symbol = Symbol(name="LostKey", look="&", location=(5, 10))

    def test_initialization(self):
        """Test that the Symbol object is initialized correctly"""
        # Check if the name, look, and location are correctly initialized
        self.assertEqual(self.symbol.name, "LostKey")
        self.assertEqual(self.symbol.look, "&")
        self.assertEqual(self.symbol.location, (5, 10))

    def test_repr(self):
        """Test the __repr__ method"""
        expected_repr = "Symbol(Name: 'LostKey', Look: '&', Location: (5, 10))"
        self.assertEqual(repr(self.symbol), expected_repr)

    def test_location_type(self):
        """Test if location is a tuple and has the correct number of elements"""
        self.assertIsInstance(self.symbol.location, tuple)
        self.assertEqual(len(self.symbol.location), 2)
        self.assertEqual(self.symbol.location[0], 5)
        self.assertEqual(self.symbol.location[1], 10)

    def test_invalid_location(self):
        """Test that an invalid location raises an error (e.g., not a tuple or wrong format)"""
        with self.assertRaises(TypeError):
            Symbol(name="InvalidSymbol", look="*", location="invalid location")
        
        with self.assertRaises(ValueError):
            Symbol(name="InvalidSymbol", look="*", location=(5, "wrong"))

if __name__ == "__main__":
    unittest.main()
