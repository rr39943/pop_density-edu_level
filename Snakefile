rule all:
    input:
        "data/processed_data/report.md",


rule clean_excel_surf_pop:
    input:
        "data/raw_data/T_02_02_1_01.xls",
        "scripts/lib/abbreviated_cantons.json",
        "scripts/lib/clean_utils.py",
        "scripts/clean_canton_surf_pop.py"
    output:
        "data/intermediate_data/cantons_surf_pop.csv"
    message:
        "From Excel file with data about cantons surface and population, create clean csv file."
    shell:
        "python scripts/clean_canton_surf_pop.py {input[0]} {output}"


rule clean_excel_univ_edu:
    input:
        "data/raw_data/su-f-40.02.15.08.03-2016.xlsx",
        "scripts/lib/abbreviated_cantons.json",
        "scripts/lib/clean_utils.py",
        "scripts/clean_canton_univ_edu.py"
    output:
        "data/intermediate_data/cantons_univ_edu.csv"
    message:
        "From Excel file with data about cantons with university level education, create clean csv file."
    shell:
        "python scripts/clean_canton_univ_edu.py {input[0]} {output}"


rule combine_csv_files:
    input:
        "data/intermediate_data/cantons_univ_edu.csv",
        "data/intermediate_data/cantons_surf_pop.csv",
        "scripts/build_dataframe.py"
    output:
        "data/processed_data/cantons_surf_pop_edu.csv"
    message:
        "Parse cleaned csv files, combine them and produce a new processed csv file."
    shell:
        "python scripts/build_dataframe.py {input[0]} {input[1]} {output}"



rule create_chart:
    input:
        "data/processed_data/cantons_surf_pop_edu.csv",
        "scripts/calculate_results.py"
    output:
        "data/processed_data/chart.png"
    message:
        "Produce comparison chart."
    shell:
        "python scripts/calculate_results.py {input[0]} --build-chart {output}"


rule create_report:
    input:
        "data/processed_data/cantons_surf_pop_edu.csv",
        "data/processed_data/chart.png",
        "scripts/calculate_results.py"
    output:
        "data/processed_data/report.md"
    message:
        "Produce final report."
    shell:
        "python scripts/calculate_results.py {input[0]} --build-report {output}"


rule clean:
    shell:
        """rm data/processed_data/*
           rm data/intermediate_data/*"""

rule rulegraph:
    shell:
        "snakemake --rulegraph | dot -Tpng > documentation/rulegraph.png"
