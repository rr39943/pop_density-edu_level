# Description of data files

## Raw Data
**data/raw_data/su-f-40.02.15.08.03-2016.xlsx:**
* Title: Population résidante permanente de 15 ans et plus, selon la formation achevée la plus élevée et le canton, en 2016
* Author: Office fédéral de la statistique (OFS), section POP
* Description: population of 15 years old and more by education level. We use the following columns:
    * "Canton"
    * "Hautes écoles": "Nombres absolus". The document provide a confidence interval that we ignored in this study.
* Creation date: 2013-05-06
* Last modified date: 2018-01-09
* URL: https://www.bfs.admin.ch/bfs/fr/home/statistiques/catalogues-banques-donnees/tableaux.assetdetail.4242918.html
* Format: xlsx

**data/raw_data/T_02_02_1_01.xls:**
* Title: Statistique de la superficie de la Suisse et population résidante, par canton
* Author: Office cantonal de la statistique - OCSTAT
* Description: area and population density, by township and statistical area of ​​the city, since 2005. We use the following columns:
    * Column A with the cantons
    * "Surface en hectare": "Surface d'habitat et d'infrastructure" and "Total"
    * "Population résidante"
* Creation date: 1999-01-29
* Last modified date: 2017-05-18
* URL: https://www.ge.ch/statistique/tel/domaines/02/02_02/T_02_02_1_01.xls
* Format: xls

## Intermediate Data
**data/intermediate_data/cantons_surf_pop.csv**
* title: cantons_surf_pop.csv
* Description: file build from the parsing of "data/raw_data/T_02_02_1_01.xls". Contains the columns "Cantons", "SurfHabAndInf", "SurfTotal", "PopTotal", "PopBySurfHabAndInf", "PopBySurfTotal". Describe the population density and the size of each canton.

**data/intermediate_data/cantons_univ_edu.csv**
* Title: cantons_univ_edu.csv
* Description: file build from the parsing of "data/raw_data/su-f-40.02.15.08.03-2016.xlsx". Contains the columns "Cantons", "UnivEdu". Mentions the number of person with a university degree.
* format: text/csv

## Processed data

**data/processed_data/cantons_surf_pop_edu.csv**
* Title: cantons_surf_pop_edu.csv
* Description: file with all the processed data. Contains the following columns: "Cantons", "UnivEdu", "SurfHabAndInf", "SurfTotal", "PopTotal", "PopBySurfHabAndInf", "PopBySurfTotal", "RatPopUnivLevel"
* format: text/csv
