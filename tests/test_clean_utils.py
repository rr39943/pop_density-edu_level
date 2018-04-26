import unittest
import sys
sys.path.append('scripts/lib')
from clean_utils import cleanUtils

class TestCleanUtils(unittest.TestCase):

    def test_read_json(self):
        """
        Switzerland has 26 cantons but the json has more keys (orthographcical variations). Check if
        the object returned has 47 keys.
        """
        self.assertEqual(len(cleanUtils._read_json('abbreviated_cantons.json')), 47)

    def test_canton_name_to_abbreviation_1(self):
        """
        Test if for "Zurich", the function return "ZH".
        """
        self.assertEqual(cleanUtils.canton_name_to_abbreviation('Zurich'), 'ZH')

    def test_canton_name_to_abbreviation_2(self):
        """
        Test if for "Neuchâtel" return "NE".
        """
        self.assertEqual(cleanUtils.canton_name_to_abbreviation('Neuchâtel'), 'NE')

    def test_convert_ha_to_km2(self):
        """
        Test if conversion of ha to km2 is working.
        """
        self.assertEqual(cleanUtils.convert_ha_to_km2(1000), 10)
