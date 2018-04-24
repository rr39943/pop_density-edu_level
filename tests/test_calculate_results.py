import unittest
import os
import pandas as pd
import numpy as np
from scripts import clean_canton_surf_pop
from scripts import clean_canton_univ_edu
from scripts import build_dataframe
from scripts import calculate_results

# Empty the "tests/test_data/" folder
file_list = os.listdir('tests/test_data/')
for f in file_list:
    if f in ['chart.png', 'report.md', 'cantons_surf_pop_edu_test.csv', 'tests/test_data/cantons_surf_pop_test2.csv', 'tests/test_data/cantons_univ_edu_test2.csv']:
        os.remove('tests/test_data/' + f)

# Create the processed csv file in the "tests/test_data/" folder
clean_canton_surf_pop.create_csv_file('data/raw_data/T_02_02_1_01.xls',
                                      'tests/test_data/cantons_surf_pop_test2.csv')
clean_canton_univ_edu.create_csv_file('data/raw_data/su-f-40.02.15.08.03-2016.xlsx',
                                      'tests/test_data/cantons_univ_edu_test2.csv')
build_dataframe.create_csv_file('tests/test_data/cantons_surf_pop_test2.csv',
                                'tests/test_data/cantons_univ_edu_test2.csv',
                                'tests/test_data/cantons_surf_pop_edu_test.csv')

calculate_results.main('tests/test_data/cantons_surf_pop_edu_test.csv',
                       '--build-chart',
                       'tests/test_data/chart.png')

calculate_results.main('tests/test_data/cantons_surf_pop_edu_test.csv',
                       '--build-report',
                       'tests/test_data/report.md')

class TestCalculateResults(unittest.TestCase):

    def test_main(self):
        """
        Test if main function create a report.
        """
        self.assertTrue(os.path.isfile('tests/test_data/report.md'))

    def test_calculate_pearson_corr(self):
        """
        Test if a string report is returned.
        """
        serie_1 = pd.Series([1, 2, 3, 4], name='serie_1')
        serie_2 = pd.Series([5, 6, 7, 8], name='serie_2')
        txt = calculate_results.pearson_corr(serie_1, serie_2)
        self.assertTrue(txt.find('*: **1.0**') > 0 and txt.find('Risk error: **0.0 %**') > 0)

    def test_create_chart(self):
        """
        Test if the chart exists.
        """
        self.assertTrue(os.path.isfile('tests/test_data/chart.png'))
