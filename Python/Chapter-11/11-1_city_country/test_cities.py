import unittest

from city_functions import city_country

class CitiesTestCase(unittest.TestCase):
    """Test for 'city_functions.py'."""
    
    def test_city_country(self):
        """Does a simple city and country pair work?"""
        santiago_chile = city_country('santiago', 'chile')
        self.assertEqual(santiago_chile, 'Santiago, Chile')

if __name__ == '__main__':
    unittest.main()