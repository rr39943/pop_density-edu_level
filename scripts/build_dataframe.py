import pandas as pd
import os
import sys
sys.path.append('scripts/lib')

def create_csv_file(file_name_source_1, file_name_source_2, file_name_dest):
    """
    Parse cleaned csv files ("data/processed_data/cantons_surf_pop.csv" and
    "data/processed_data/cantons_univ_edu.csv") and produce a new processed
    csv file.
    """
    df1 = pd.read_csv(file_name_source_1)
    df2 = pd.read_csv(file_name_source_2)
    df = df1.merge(df2, on='Cantons')

    df['RatPopUnivLevel'] = df['UnivEdu'] / df['PopTotal']

    # Test if destination folder exists, if not creates it
    if not(os.path.isdir(os.path.dirname(file_name_dest))):
        os.makedirs(os.path.dirname(file_name_dest))

    df.to_csv(file_name_dest, index=False)

if __name__ == '__main__':
    create_csv_file(sys.argv[1], sys.argv[2], sys.argv[3])
