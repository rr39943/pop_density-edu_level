import sys
import os
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy import stats


def pearson_corr(serie_1, serie_2):
    """
    Caculate the pearson correlation of the two provided series and return a text
    to be integrated in the report.
    """
    p_corr = stats.pearsonr(serie_1.values, serie_2.values)
    txt = """___\n\nPearson correlation between *{}* and *{}*: **{}**\n
* Risk error: **{} %** \n\n""".format(serie_1.name,
                             serie_2.name,
                             np.around(p_corr[0], 3),
                             np.around(p_corr[1]*100, 4))
    return txt


def create_report(file_name_source, file_name_dest):
    """
    Parse cleaned csv files ("data/processed_data/cantons_surf_pop.csv" and
    "data/processed_data/cantons_univ_edu.csv") and produce a new processed
    csv file.
    """

    # Variable to store report string
    txt = '# Analysis Results\n\n'

    # read the data
    df = pd.read_csv(file_name_source)

    txt += pearson_corr(df['RatPopUnivLevel'], df['PopBySurfTotal'])

    txt += pearson_corr(df['RatPopUnivLevel'], df['PopBySurfHabAndInf'])

    txt += """____\n\n![chart](./data/processed_data/chart.png)"""

    # Test if destination folder exists, if not creates it
    if not(os.path.isdir(os.path.dirname(file_name_dest))):
        os.makedirs(os.path.dirname(file_name_dest))

    # create report file
    with open(file_name_dest, 'w') as f:
        f.write(txt)
    # print(RatPopUnivLevel_PopBySurfTotal, RatPopUnivLevel_SurfHabAndInf)

def create_subplot(**kwargs):
    """
    Create one subplot.
    """
    line_label = 'Part of pop. with university diploma'
    kwargs['graph'].set_title(kwargs['chart_title'])
    bars = kwargs['graph'].bar(range(26), kwargs['df'].iloc[:,-1].values, color='blue', width=0.6, alpha=0.5)
    kwargs['graph'].set_xticks(range(26))
    kwargs['graph'].set_xticklabels(kwargs['df']['Cantons'].values)
    ax_bis = kwargs['graph'].twinx()
    line = ax_bis.plot(range(26), kwargs['df']['RatPopUnivLevel'].values, color='r', linewidth=3)
    kwargs['graph'].set_xlabel('Cantons')
    kwargs['graph'].set_ylabel(kwargs['bars_label'])
    ax_bis.set_ylabel(line_label)
    ax_bis.set_ylim(ymin=0)
    ax_bis.set_yticklabels(['{:2.0f}%'.format(x*100) for x in ax_bis.get_yticks()])
    plt.legend((bars[0], line[0]), (kwargs['bars_label'], line_label))


def create_chart(file_name_source, file_name_dest):
    """
    Create a chart with the population of canton by km2 and the part of the population
    with a university diploma.
    """

    # Sort the row by pop. density
    df1 = pd.read_csv(file_name_source).sort_values(by='PopBySurfTotal', ascending=False).copy()
    df2 = df1.copy().sort_values(by='PopBySurfHabAndInf', ascending=False)

    fig = plt.figure(figsize=(12, 12))

    # First subplot
    ax1 = fig.add_subplot(211)
    ax1 = create_subplot(graph=ax1,
                         df=df1.loc[:,['Cantons', 'RatPopUnivLevel', 'PopBySurfTotal']],
                         bars_label = 'Pop. by km2',
                         chart_title='Comparison: density pop. vs part of pop. with university diploma')

    # Second subplot
    ax2 = fig.add_subplot(212)
    ax2 = create_subplot(graph=ax2,
                         df=df2.loc[:,['Cantons', 'RatPopUnivLevel', 'PopBySurfHabAndInf']],
                         bars_label='Pop. by km2 (habitable and infrastructure)',
                         chart_title='Comparison: density pop. (habitable and infrastructure part) vs part of pop. with university diploma')

    plt.savefig(file_name_dest)


def main(file_name_source, action, file_name_dest):
    """
    Calculate results:
    - action "--build-report": calculate Pearson correlation between
    - action "--build-graph": build png chart
    """
    if action == '--build-report':
        create_report(file_name_source, file_name_dest)
    if action == '--build-chart':
        create_chart(file_name_source, file_name_dest)

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
