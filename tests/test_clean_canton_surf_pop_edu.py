import unittest
import os
import pandas as pd
import numpy as np
from scripts import clean_canton_surf_pop
from scripts import clean_canton_univ_edu
from scripts import build_dataframe

# Empty the "tests/test_data/" folder
file_list = os.listdir('tests/test_data/')
for f in file_list:
    if f in ['cantons_surf_pop_edu.csv', 'tests/test_data/cantons_surf_pop_test.csv', 'tests/test_data/cantons_univ_edu_test.csv']:
        os.remove('tests/test_data/' + f)

# Create the processed csv file in the "tests/test_data/" folder
clean_canton_surf_pop.create_csv_file('data/raw_data/T_02_02_1_01.xls',
                                      'tests/test_data/cantons_surf_pop_test.csv')
clean_canton_univ_edu.create_csv_file('data/raw_data/su-f-40.02.15.08.03-2016.xlsx',
                                      'tests/test_data/cantons_univ_edu_test.csv')
build_dataframe.create_csv_file('tests/test_data/cantons_surf_pop_test.csv',
                                'tests/test_data/cantons_univ_edu_test.csv',
                                'tests/test_data/cantons_surf_pop_edu.csv')

class TestCleanCantonSurfPopEdu(unittest.TestCase):

    def test_create_csv(self):
        """
        Test if a csv file is created.
        """
        self.assertTrue(os.path.isfile('tests/test_data/cantons_surf_pop_edu.csv'))

    def test_columns_csv(self):
        """
        Test if the second column is "UnivEdu".
        """
        list_cols = pd.read_csv('tests/test_data/cantons_surf_pop_edu.csv').columns
        self.assertEqual(len(list_cols), 8)

    def test_parse_csv_length(self):
        """
        Test if there are 26 rows in the processed file corresponding to the 26 cantons.
        """
        df = pd.read_csv('tests/test_data/cantons_surf_pop_edu.csv')
        self.assertEqual(len(df.index), 26)
