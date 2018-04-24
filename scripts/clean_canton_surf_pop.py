import pandas as pd
import numpy as np
import sys
sys.path.append('scripts/lib')
from clean_utils import cleanUtils

def create_csv_file(file_name_source, file_name_dest):
    """
    Parse the Excel sheet provided and extract the total of population of cantons,
    habitable surface and total surface.
    It is working only with data/raw_data/su-f-01.02.04.04.xlsx. It create a csv
    file with the cantons abbreviated and the total of population.
    """
    df = pd.read_excel(file_name_source,
                       skiprows=14,
                       skip_footer=9,
                       usecols=[0, 5, 7, 9],
                       names=['Cantons', 'SurfHabAndInf', 'SurfTotal', 'PopTotal'])
    df['Cantons'] = df['Cantons'].apply(cleanUtils.canton_name_to_abbreviation)
    df['SurfHabAndInf'] = df['SurfHabAndInf'].apply(cleanUtils.convert_ha_to_km2)
    df['SurfTotal'] = df['SurfTotal'].apply(cleanUtils.convert_ha_to_km2)
    df['PopBySurfHabAndInf'] = df['PopTotal'] / df['SurfHabAndInf']
    df['PopBySurfTotal'] = df['PopTotal'] / df['SurfTotal']


    df.to_csv(file_name_dest, index=False)


if __name__ == '__main__':
    create_csv_file(sys.argv[1], sys.argv[2])
