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
                             np.around(p_corr[1]*100, 3))
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

    txt += pearson_corr(df['RatPopUnivLevel'], df['SurfHabAndInf'])

    txt += """____\n\n![chart](./data/processed_data/chart.png)"""

    if not(os.path.isdir(os.path.dirname(file_name_dest))):
        os.makedirs(os.path.dirname(file_name_dest))

    # create report file
    with open(file_name_dest, 'w') as f:
        f.write(txt)
    # print(RatPopUnivLevel_PopBySurfTotal, RatPopUnivLevel_SurfHabAndInf)


def create_chart(file_name_source, file_name_dest):
    """
    Create a chart with the population of canton by km2 and the part of the population
    with a university diploma.
    """
    chart_title = 'Comparison: size of canton and pop. with university diploma'
    line_label = 'Part of pop. with university diploma'
    bars_label = 'Pop. by km2'

    df = pd.read_csv(file_name_source)
    df = df.sort_values(by='PopBySurfTotal', ascending=False)

    # Sort the row by pop. density
    df1 = df.sort_values(by='PopBySurfTotal', ascending=False).copy()
    df2 = df.sort_values(by='PopBySurfHabAndInf', ascending=False).copy()

    chart_title1 = 'Comparison: density pop. vs part of pop. with university diploma'
    chart_title2 = 'Comparison: density pop. (habitable and infrastructure part) vs part of pop. with university diploma'
    line_label = 'Part of pop. with university diploma'
    bars_label1 = 'Pop. by km2'
    bars_label2 = 'Pop. by km2 (habitable and infrastructure)'

    fig = plt.figure(figsize=(12, 12))
    ax1 = fig.add_subplot(211)
    ax1.set_title(chart_title1)
    bars1 = ax1.bar(range(26), df1['PopBySurfTotal'].values, color='blue', width=0.6, alpha=0.5, label=bars_label)
    ax1.set_xticks(range(26))
    ax1.set_xticklabels(df1['Cantons'].values)
    ax2 = ax1.twinx()
    line1 = ax2.plot(range(26), df1['RatPopUnivLevel'].values, color='r', linewidth=3, label=line_label)
    ax1.set_xlabel('Cantons')
    ax1.set_ylabel(bars_label1)
    ax2.set_ylabel(line_label)
    ax2.set_ylim(ymin=0)
    vals = ax2.get_yticks()
    ax2.set_yticklabels(['{:2.0f}%'.format(x*100) for x in vals])
    plt.legend((bars1[0], line1[0]), (bars_label1, line_label))

    ax3 = fig.add_subplot(212)
    ax3.set_title(chart_title2)
    bars2 = ax3.bar(range(26), df2['PopBySurfHabAndInf'].values, color='blue', width=0.6, alpha=0.5, label=bars_label)
    ax3.set_xticks(range(26))
    ax3.set_xticklabels(df2['Cantons'].values)
    ax4 = ax3.twinx()
    line2 = ax4.plot(range(26), df2['RatPopUnivLevel'].values, color='r', linewidth=3, label=line_label)
    ax3.set_xlabel('Cantons')
    ax3.set_ylabel(bars_label2)
    ax4.set_ylabel(line_label)
    ax4.set_ylim(ymin=0)
    vals = ax4.get_yticks()
    ax4.set_yticklabels(['{:2.0f}%'.format(x*100) for x in vals])
    plt.legend((bars1[0], line1[0]), (bars_label2, line_label))

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
