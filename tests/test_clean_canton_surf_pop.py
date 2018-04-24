import unittest
import os
import pandas as pd
from scripts import clean_canton_surf_pop

# Empty the "tests/test_data/" folder
file_list = os.listdir('tests/test_data/')
for f in file_list:
    if f == 'cantons_surf_pop.csv':
        os.remove('tests/test_data/' + f)

# Create the processed csv file in the "tests/test_data/" folder
clean_canton_surf_pop.create_csv_file('data/raw_data/T_02_02_1_01.xls',
                                      'tests/test_data/cantons_surf_pop.csv')

class TestCleanCantonSurfPop(unittest.TestCase):

    def test_create_csv(self):
        """
        Test if a csv file is created.
        """
        self.assertTrue(os.path.isfile('tests/test_data/cantons_surf_pop.csv'))

    def test_columns_csv(self):
        """
        Test if the 4th column is "PopTotal".
        """
        list_cols = pd.read_csv('tests/test_data/cantons_surf_pop.csv').columns
        self.assertEqual(list_cols[3], 'PopTotal')

    def test_parse_csv_pop(self):
        """
        Test if the processed file contains 54543 for canton AR (Appenzell Rh.-Ext.).
        """
        df = pd.read_csv('tests/test_data/cantons_surf_pop.csv')
        self.assertEqual(df.loc[df['Cantons']=='AR', 'PopTotal'].values[0], 54543)

    def test_parse_csv_surf(self):
        """
        Test if the processed file contains 16714400 ha for canton FR (Fribourg).
        """
        df = pd.read_csv('tests/test_data/cantons_surf_pop.csv')
        self.assertEqual(df.loc[df['Cantons']=='FR', 'SurfTotal'].values[0], 1671.44)

    def test_parse_csv_length(self):
        """
        Test if there are 26 rows in the processed file corresponding to the 26 cantons.
        """
        df = pd.read_csv('tests/test_data/cantons_surf_pop.csv')
        self.assertEqual(len(df.index), 26)
