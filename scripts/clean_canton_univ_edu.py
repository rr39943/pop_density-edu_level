import pandas as pd
import numpy as np
import sys
import os
sys.path.append('scripts/lib')
from clean_utils import cleanUtils

def create_csv_file(file_name_source, file_name_dest):
    """
    Parse the Excel sheet provided and extract the total of persons who have a
    diploma of a university. It is working only with data/raw_data/T_02_02_1_01.xls.
    It create a csv file with the cantons abbreviated and highest formation.
    """
    df = pd.read_excel(file_name_source,
                       skiprows=4,
                       skip_footer=10,
                       usecols=[2, 13],
                       names=['Cantons', 'UnivEdu'])

    # Get digrams for the cantons
    df['Cantons'] = df['Cantons'].apply(cleanUtils.canton_name_to_abbreviation)

    # Test if destination folder exists, if not creates it
    if not(os.path.isdir(os.path.dirname(file_name_dest))):
        os.makedirs(os.path.dirname(file_name_dest))

    df.to_csv(file_name_dest, index=False)


if __name__ == '__main__':
    create_csv_file(sys.argv[1], sys.argv[2])
